"""Check for item 2 of 06-ilang-source/08-typical-or-forced (role: check).

One field object (N_f = 1, n = 1/|X|) of class F with r = 2 internal places on a ring (D = 1)
or a square torus (D = 2) of side L. Own contract h = sum_a sum_x |x+a><x| (x) h_a with Bloch
matrix h(k) = -2t sum_mu cos k_mu + Delta |2><2| + lam sin k_1 sigma_1 (lowest state at k_0 = 0),
coupled operator Phi_x = |x><x| (x) phi, source at x_s = 0.
chi_0(x, x_s) of (3.6) is computed from the eigenvectors of h and compared with the Bloch formula
(8.8) and with the large-distance forms (8.10), (8.11), (8.13). All values are reported as chi/(2n).
On the tori, L = 20, 32 use full diagonalization; L = 64 uses (8.8) only (checked at L = 20, 32).
Maximal deviations are logged over stated distance windows: against the lattice form of the leading
term at the same L, and (member phibar0) against the L -> infinity value of the leading term.
"""
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
T, DELTA = 1.0, 1.5
SX = np.array([[0, 1], [1, 0]], complex)
P2 = np.diag([0, 1]).astype(complex)
PHI_LR = np.array([[1.0, 0.3], [0.3, -0.5]], complex)
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


def blocks(D, lam):
    """Hopping blocks h_a of h = sum_a sum_x |x+a><x| (x) h_a, h(k) = sum_a exp(-i k.a) h_a."""
    b = {(0,) * D: DELTA * P2}
    for mu in range(D):
        e = np.zeros(D, int)
        e[mu] = 1
        hp = -T * np.eye(2, dtype=complex) + (0.5j * lam * SX if mu == 0 else 0)
        b[tuple(e)] = hp
        b[tuple(-e)] = hp.conj().T
    return b


def h_bloch(k, blk):
    return sum(np.exp(-1j * np.dot(k, a)) * M for a, M in blk.items())


def lowest(blk, k):
    ev, W = np.linalg.eigh(h_bloch(k, blk))
    return ev[0], W[:, 0]


def grid(L, D):
    return np.array(np.unravel_index(np.arange(L ** D), (L,) * D)).T


def chi_direct(L, D, blk, phi):
    """chi_0(x, 0) of (3.6) from the full diagonalization of h on |X| x r places."""
    n, xs = L ** D, grid(L, D)
    H = np.zeros((2 * n, 2 * n), complex)
    for a, M in blk.items():
        tgt = np.ravel_multi_index(((xs + np.array(a)) % L).T, (L,) * D)
        for s in range(n):
            H[2 * tgt[s]:2 * tgt[s] + 2, 2 * s:2 * s + 2] += M
    assert np.allclose(H, H.conj().T)
    e, U = np.linalg.eigh(H)
    assert e[1] - e[0] > 1e-8, "lowest eigenvector not unique"
    Ur = U.reshape(n, 2, -1)
    amp = np.einsum("xo,op,xpm->xm", Ur[:, :, 0].conj(), phi, Ur)  # <u_0|phi_x|u_m>
    chi = 2 * np.real(amp[:, 1:] * amp[0, 1:].conj()) @ (1 / (e[1:] - e[0]))
    return chi.reshape((L,) * D)


def chi_bloch(L, D, blk, phi):
    """(8.8) with k_0 = 0: chi(d) = (2n/|X|) sum_q cos(q.d) S_L(q)."""
    e0, w0 = lowest(blk, np.zeros(D))
    S = np.empty(L ** D)
    for i, k in enumerate(2 * np.pi * grid(L, D) / L):
        ev, W = np.linalg.eigh(h_bloch(k, blk))
        m2 = np.abs(W.conj().T @ phi @ w0) ** 2
        keep = ev - e0 > 1e-12  # drops only (k_0, l = 0)
        S[i] = np.sum(m2[keep] / (ev[keep] - e0))
    return 2 / L ** D * np.real(np.fft.ifftn(S.reshape((L,) * D)))


def band_data(D, blk, phi, eps=1e-3):
    """phibar = <w0|phi|w0>; A = Hessian/2 of the lowest band at k_0; C = Hessian/2 of |F(q)|^2."""
    _, w0 = lowest(blk, np.zeros(D))
    phibar = np.real(w0.conj() @ phi @ w0)
    E = lambda q: lowest(blk, q)[0]  # noqa: E731
    F2 = lambda q: abs(w0.conj() @ phi @ lowest(blk, q)[1]) ** 2  # noqa: E731
    A, C = np.zeros((D, D)), np.zeros((D, D))
    for mu in range(D):
        for nu in range(D):
            em, en = np.eye(D)[mu] * eps, np.eye(D)[nu] * eps
            for f, Mat in ((E, A), (F2, C)):
                Mat[mu, nu] = (f(em + en) - f(em - en) - f(en - em) + f(-em - en)) / (8 * eps ** 2)
    return phibar, A, C


def pred_lattice(L, D, ratio):
    """(1/|X|) sum_{q != 0} cos(q.d) ratio(qhat), qhat_mu = 2 sin(q_mu/2): lattice form of chi/(2n)."""
    qh = 2 * np.sin(np.pi * grid(L, D) / L)
    val = np.array([ratio(v) if np.any(v != 0) else 0.0 for v in qh])
    return np.real(np.fft.ifftn(val.reshape((L,) * D)))


def osc(c):
    """Omega(d) = max - min of c over graph distances d..L/2."""
    return np.array([c[i:].max() - c[i:].min() for i in range(len(c))])


rows_ring, rows_torus = [], []
fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))
log("Check of item 2: chi_0(x, x_s) of (3.6) for one field object (N_f = 1), r = 2, x_s = 0.")
log(f"t = {T}, Delta = {DELTA}; all values are chi/(2n), n = 1/|X|.")

# ---------------- rings ----------------
ring = {"LR": (0.5, PHI_LR), "phibar0": (0.5, SX), "sector": (0.0, SX)}
styles = {"LR": "-", "phibar0": "--", "sector": ":"}
for name, (lam, phi) in ring.items():
    blk = blocks(1, lam)
    phibar, A, C = band_data(1, blk, phi)
    a = A[0, 0]
    log(f"\n[ring] member {name}: lam = {lam}, phibar = {phibar:.6f}, A = {a:.6f} "
        f"(analytic t - lam^2/Delta = {T - lam ** 2 / DELTA:.6f}), C = {C[0, 0]:.6f}")
    for L in (40, 80, 160):
        chi = chi_direct(L, 1, blk, phi)
        err = np.max(np.abs(chi - chi_bloch(L, 1, blk, phi))) * L / 2
        c = chi[: L // 2 + 1] * L / 2
        d = np.arange(L // 2 + 1)
        om = osc(c)
        msg = f"  L = {L:4d}: max |direct - Bloch (8.8)| = {err:.2e}; Omega(L/4) = {om[L // 4]:.3e}"
        if name == "LR":
            p = pred_lattice(L, 1, lambda q: phibar ** 2 / (a * q[0] ** 2))[: L // 2 + 1]
            sel = slice(6, L // 2 - 5)
            r = (c[sel] - c[-1]) / (p[sel] - p[-1])
            msg += (f"; (chi(d)-chi(L/2))/(pred(d)-pred(L/2)) over 6<=d<=L/2-6: "
                    f"max|ratio-1| = {np.max(np.abs(r - 1)):.2e}; slope -(chi(12)-chi(8))/4 = "
                    f"{-(c[12] - c[8]) / 4:.4f} vs phibar^2/(2A)(1-20/L) = "
                    f"{phibar ** 2 / (2 * a) * (1 - 20 / L):.4f}")
        elif name == "phibar0":
            kap = np.arccosh((4 * T ** 2 + 2 * T * DELTA - lam ** 2) / (4 * T ** 2 + lam ** 2))
            fit = -np.polyfit(d[4:15], np.log(np.abs(c[4:15] - c[-1])), 1)[0]
            msg += (f"; chi(L/2)/(2n) = {c[-1]:.3e} (O(1/L) constant); fitted decay rate of "
                    f"|chi(d)-chi(L/2)| (4<=d<=14) = {fit:.5f} vs nearest zero of det(h(k)-e0): {kap:.5f}")
        else:
            kap = np.arccosh(1 + DELTA / (2 * T))
            ex = np.cosh(kap * (L / 2 - d)) / (2 * T * np.sinh(kap) * np.sinh(kap * L / 2))
            msg += f"; max|chi/(2n) - exact (8.13)| = {np.max(np.abs(c - ex)):.2e} (kappa = {kap:.5f})"
        log(msg)
        for di in d:
            rows_ring.append((name, L, di, c[di], om[di]))
        if L in (40, 160):
            ax[0].semilogy(d[:-1], om[:-1], styles[name], label=f"{name}, L={L}")

# ---------------- tori ----------------
torus = {"LR": (0.5, PHI_LR), "phibar0": (0.5, SX)}
for name, (lam, phi) in torus.items():
    blk = blocks(2, lam)
    phibar, A, C = band_data(2, blk, phi)
    a1, a2 = A[0, 0], A[1, 1]
    log(f"\n[torus] member {name}: lam = {lam}, phibar = {phibar:.6f}, A = diag({a1:.6f}, {a2:.6f}) "
        f"(offdiag {A[0, 1]:.1e}), C = [[{C[0, 0]:.6f}, {C[0, 1]:.1e}], [., {C[1, 1]:.1e}]]")
    for L in (20, 32, 64):
        chib = chi_bloch(L, 2, blk, phi)
        if L <= 32:
            chi = chi_direct(L, 2, blk, phi)
            log(f"  L = {L}: max |direct - Bloch (8.8)| = {np.max(np.abs(chi - chib)) * L ** 2 / 2:.2e}")
        else:
            chi = chib
            log(f"  L = {L}: chi from the Bloch formula (8.8) only")
        c = chi * L ** 2 / 2
        if name == "LR":
            p = pred_lattice(L, 2, lambda q: phibar ** 2 / (a1 * q[0] ** 2 + a2 * q[1] ** 2))
        else:
            p = pred_lattice(L, 2, lambda q: (q @ C @ q) / (a1 * q[0] ** 2 + a2 * q[1] ** 2))
        for axis in (0, 1):
            d = np.arange(L // 2 + 1)
            cd = c[d, 0] if axis == 0 else c[0, d]
            pd = p[d, 0] if axis == 0 else p[0, d]
            for di in d:
                rows_torus.append((name, L, axis + 1, di, cd[di], pd[di]))
            if name == "LR":
                ref = L // 2
                w = np.arange(3, L // 4 + 1)
                r = (cd[w] - cd[ref]) / (pd[w] - pd[ref])
                log(f"    axis {axis + 1}: ratio (chi(d)-chi(L/2))/(pred(d)-pred(L/2)), pred = lattice form of "
                    f"phibar^2/(q^T A q) at the same L: d=3: {r[0]:.4f}, d=L/4={L // 4}: {r[-1]:.4f}; "
                    f"max|ratio-1| over 3<=d<=L/4 = {np.max(np.abs(r - 1)):.4f}")
            else:
                cc, pc = c[L // 2, L // 2], p[L // 2, L // 2]  # far corner as reference
                k_inf = (-C[0, 0] / (2 * np.pi * np.sqrt(a1 * a2)) if axis == 0
                         else C[0, 0] * np.sqrt(a2) / (2 * np.pi * a1 ** 1.5))
                Dd, Pd = d ** 2 * (cd - cc), d ** 2 * (pd - pc)
                s = ", ".join(f"d={di}: {Dd[di]:+.5f} (pred {Pd[di]:+.5f})" for di in (4, 6, 8, 10))
                w1 = np.arange(8, L // 2 - 1)
                msg = (f"    axis {axis + 1}: d^2 (chi(d)-chi(corner))/(2n), pred = lattice form of "
                       f"q^T C q/(q^T A q) at the same L: {s}; L -> infinity value of d^2 chi/(2n) = "
                       f"-C11 d^2 (d/dd1)^2 G_A = {k_inf:+.5f}; max rel. dev. from the same-L lattice form "
                       f"over 8<=d<=L/2-2: {np.max(np.abs(Dd[w1] / Pd[w1] - 1)):.3f}")
                if L >= 64:
                    w2, w3 = np.arange(16, L // 2 - 1), np.arange(8, L // 5 + 1)
                    msg += (f", over 16<=d<=L/2-2: {np.max(np.abs(Dd[w2] / Pd[w2] - 1)):.3f}; "
                            f"max rel. dev. from the L -> infinity value over 8<=d<=L/5={L // 5}: "
                            f"{np.max(np.abs(Dd[w3] / k_inf - 1)):.3f}")
                log(msg)
                if L == 64:
                    dd = d[2:]
                    ln = ax[1].plot(dd, dd ** 2 * (cd[2:] - cc), "o", label=f"direct, axis {axis + 1}")
                    ax[1].plot(dd, dd ** 2 * (pd[2:] - pc), "-", color=ln[0].get_color(),
                               label=f"lattice form of (8.11), axis {axis + 1}")
                    ax[1].axhline(k_inf, ls=":", color=ln[0].get_color())

ax[0].set_xlabel("graph distance d from the source (ring)")
ax[0].set_ylabel("Omega(d)/(2n) = max-min of chi/(2n) beyond d")
ax[0].legend(fontsize=7)
ax[1].set_xlabel("d along axis (torus L=64, member phibar0)")
ax[1].set_ylabel("d^2 (chi(d) - chi(corner))/(2n)")
ax[1].legend(fontsize=7)
fig.tight_layout()
fig.savefig(OUT / "decay.png", dpi=120)
np.savetxt(OUT / "chi_ring.csv", np.array(rows_ring, dtype=object), fmt="%s", delimiter=",",
           header="member,L,d,chi_over_2n,Omega_over_2n", comments="")
np.savetxt(OUT / "chi_torus.csv", np.array(rows_torus, dtype=object), fmt="%s", delimiter=",",
           header="member,L,axis,d,chi_over_2n,lattice_pred_over_2n", comments="")
(OUT / "check_log.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
