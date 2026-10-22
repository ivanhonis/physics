"""Check of 05-inertia-of-mark (v3): fall of the full grip from rest, (5.14), for the chart mean position, N_f = 1.

Joint description: body place x, branch, one field object y on a ring of L places; full-grip contract on
level k plus a held source g_s P_{x_s}. The start is the dressed band state with real envelope phi_j:
Psi = U sum_j phi_j |j,sigma> Omega_sigma(j), U the direct rotation (Schrieffer-Wolff) of the held band
onto the spectral band of the full contract. The observable is the chart position X = diag(0, ..., L-1) of
the body: the labels close across the cut bond (L-1, 0), opposite the start (centre L/2 - 1).
a(0) = d^2 <X>/dlambda^2 at 0 is computed from the double commutator -<[C,[C,X]]> and from the joint
evolution (second difference of <X>(lambda)); it is compared with -E''(0) sum_j phi_{j+1} phi_{j-1} W'(j),
E'' the exact curvature of the sector contract at g_s = 0, W(j) = g_s <Omega(j)|P_{x_s}|Omega(j)> the held
weight. The split a = <i[C, v]> + eps_cut, v the oriented-bond velocity (translation invariant) and
eps_cut = -L <i[C, v_cut]>, is checked, with the bound |eps_cut| <= L tau (tau + N_f|g|) p_c, p_c the weight
of the start on the body places L-2, L-1, 0, 1.
Output: output/check_fall_full_grip.txt
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
lines = []


def log(s=""):
    lines.append(s)


tf = 1.0
sx = np.array([[0, 1], [1, 0]], complex)
sz = np.diag([1.0, -1.0]).astype(complex)


def P(L, r):
    M = np.zeros((L, L)); M[r % L, r % L] = 1.0
    return M


def c1(L):
    Tp = np.roll(np.eye(L), 1, axis=0)                     # Tp |x> = |x+1>
    return Tp, -tf * (Tp + Tp.T)


def curvature(L, g, tau, sig):
    """Exact curvature at P = 0 of the dressed level of (5.1) (full grip, g_s = 0) and the tau = 0 distance d."""
    Tp, h0 = c1(L)
    C0 = np.kron(np.eye(2), h0) + g * np.kron(sz, P(L, 0))
    Cp = 0.5 * tau * np.kron(-1j * sx, Tp.T)
    w0 = np.linalg.eigvalsh(C0)
    e, V = np.linalg.eigh(h0 + sig * g * P(L, 0)); phi = V[:, 0] * np.sign(V[0, 0])
    j = np.argmin(abs(w0 - e[0])); d = np.min(abs(np.delete(w0, j) - e[0]))
    C = C0 + Cp + Cp.conj().T
    d1 = -1j * Cp + 1j * Cp.conj().T
    d2 = -(Cp + Cp.conj().T)
    wc, Vc = np.linalg.eigh(C)
    i = np.argmax(abs(Vc.conj().T @ np.kron(np.eye(2)[:, 0 if sig > 0 else 1], phi))); psi = Vc[:, i]
    a = Vc.conj().T @ (d1 @ psi); m = np.arange(len(wc)) != i
    return np.real(psi.conj() @ d2 @ psi) + 2 * np.sum(abs(a[m]) ** 2 / (wc[i] - wc[m])), d, phi


def fall(L, g, sig, tau_over_d, gs, wid, xs=0):
    j0 = L // 2 - 1
    _, d, phi = curvature(L, g, 1e-5, sig)
    tau = tau_over_d * d
    E2, _, _ = curvature(L, g, tau, sig)
    Tp, h0 = c1(L)
    I2L, IL = np.eye(2 * L), np.eye(L)
    A = 0.5 * tau * np.kron(np.kron(Tp, -1j * sx), IL); A = A + A.conj().T
    C = A + np.kron(I2L, h0 + gs * P(L, xs))
    for x in range(L):
        C = C + g * np.kron(np.kron(P(L, x), sz), P(L, x))
    X = np.kron(np.kron(np.diag(np.arange(L, dtype=float)), np.eye(2)), IL)   # chart position, cut (L-1, 0)
    v = -0.5 * tau * np.kron(np.kron(Tp + Tp.T, sx), IL)                         # oriented-bond velocity
    Ecut = np.zeros((L, L)); Ecut[0, L - 1] = 1.0
    vcut = -0.5 * tau * np.kron(np.kron(Ecut + Ecut.T, sx), IL)
    ident = np.max(abs(1j * (C @ X - X @ C) - (v - L * vcut)))                  # i[C, X] = v - L v_cut
    b = 0 if sig > 0 else 1
    held = []
    for j in range(L):
        e, V = np.linalg.eigh(h0 + sig * g * P(L, j) + gs * P(L, xs))
        held.append(np.kron(np.kron(IL[:, j], np.eye(2)[:, b]), V[:, 0] * np.sign(V[j, 0])))
    Pi = np.array(held).T
    wc, Vc = np.linalg.eigh(C)
    band = np.argsort(np.sum(abs(Vc.conj().T @ Pi) ** 2, axis=1))[-L:]
    Vb, wb = Vc[:, band], wc[band]
    Mo = Pi.conj().T @ Vb
    ev, EV = np.linalg.eigh(Mo @ Mo.conj().T)
    phij = np.exp(-(np.arange(L) - j0) ** 2 / (2 * wid * wid)); phij /= np.linalg.norm(phij)
    cb = Mo.conj().T @ (EV @ np.diag(ev ** -0.5) @ EV.conj().T @ phij)          # band coefficients of Psi
    Psi = Vb @ cb

    def ex(O):
        return np.real(Psi.conj() @ (O @ Psi))
    a_comm = -ex(C @ (C @ X) - 2 * C @ (X @ C) + (X @ C) @ C)
    a_bond = ex(1j * (C @ v - v @ C))
    eps = -L * ex(1j * (C @ vcut - vcut @ C))
    lam = 0.02 / abs(E2)

    def xmean(l):
        ps = Vb @ (np.exp(-1j * wb * l) * cb)
        return np.real(ps.conj() @ (X @ ps))
    a_evol = (xmean(lam) + xmean(-lam) - 2 * xmean(0.0)) / lam ** 2
    body = np.sum(abs(Psi.reshape(L, 2 * L)) ** 2, axis=1)                       # body-place distribution
    pc = body[[L - 2, L - 1, 0, 1]].sum()
    W = np.array([gs * phi[(xs - j) % L] ** 2 for j in range(L)])
    pred = -E2 * sum(phij[(j + 1) % L] * phij[(j - 1) % L] * 0.5 * (W[(j + 1) % L] - W[(j - 1) % L]) for j in range(L))
    bound = L * tau * (tau + abs(g)) * pc
    return dict(d=d, tau=tau, a=a_comm, evol=a_evol, bond=a_bond, eps=eps, pred=pred, pc=pc,
                bound=bound, ident=ident, split=abs(a_comm - a_bond - eps) / abs(pred))


log("(5.14) for the chart mean position: full grip, N_f = 1, t_f = 1, source at x_s = 0, Gaussian envelope")
log("centred at L/2 - 1, chart labels 0..L-1 (cut bond (L-1, 0), opposite the start).")
log("a = -<[C,[C,X]]>; evol = second difference of <X>(lambda), lambda = 0.02/|E''|; pred = -E'' sum phi phi W'.")
log("rel = a/pred - 1; rel_0 = 2 rel(g_s) - rel(2 g_s) (part surviving g_s -> 0), lin = rel(2 g_s) - rel(g_s).")
log("eps = -L<i[C, v_cut]> (boundary term), bound = L tau (tau + |g|) p_c, p_c = weight of the body on L-2..1.")
log("split = |a - <i[C, v]> - eps| / |pred|; ident = max |i[C,X] - (v - L v_cut)|.")
log()
log("1. Start localized away from the cut: width 1.0, L = 16, 20.")
mx = dict(rel=0, evol=0, eps=0, bound=0, split=0, ident=0)
for L in (16, 20):
    for g in (0.1, 0.3):
        for sig in (-1, 1):
            for tod in (0.1, 0.05):
                r1, r2 = [fall(L, g, sig, tod, gs, 1.0) for gs in (1e-3, 2e-3)]
                q1 = r1["a"] / r1["pred"] - 1; q2 = r2["a"] / r2["pred"] - 1
                ev = max(abs(r["evol"] / r["a"] - 1) for r in (r1, r2))
                eb = max(abs(r["eps"] / r["pred"]) for r in (r1, r2))
                bb = max(abs(r["bound"] / r["pred"]) for r in (r1, r2))
                mx["rel"] = max(mx["rel"], abs(q1), abs(q2)); mx["evol"] = max(mx["evol"], ev)
                mx["eps"] = max(mx["eps"], eb); mx["bound"] = max(mx["bound"], bb)
                mx["split"] = max(mx["split"], r1["split"], r2["split"]); mx["ident"] = max(mx["ident"], r1["ident"])
                log("  L=%2d gM=%.1f sig=%+d tau/d=%.2f d=%.4f | g_s=1e-3: a=%+.6e pred=%+.6e rel=%+.2e |"
                    " g_s=2e-3: rel=%+.2e | rel_0=%+.2e lin=%+.2e | |evol/a-1|=%.1e |eps/pred|=%.1e bound/pred=%.1e"
                    % (L, g, sig, tod, r1["d"], r1["a"], r1["pred"], q1, q2, 2 * q1 - q2, q2 - q1, ev, eb, bb))
log("  max |rel| = %.2e, max |evol/a - 1| = %.1e, max |eps/pred| = %.1e, max bound/pred = %.1e,"
    " max split = %.1e, max ident = %.1e" % (mx["rel"], mx["evol"], mx["eps"], mx["bound"], mx["split"], mx["ident"]))
log()
log("2. Boundary term for a start reaching the cut: width 1.5, gM = 0.1, tau/d = 0.1, g_s = 1e-3.")
for L in (12, 16):
    for sig in (-1, 1):
        r = fall(L, 0.1, sig, 0.1, 1e-3, 1.5)
        log("  L=%2d sig=%+d: a/pred-1=%+.2e, <i[C,v]>/pred-1=%+.2e, eps/pred=%+.2e,"
            " bound/|eps|=%.1e, p_c=%.1e, split=%.1e"
            % (L, sig, r["a"] / r["pred"] - 1, r["bond"] / r["pred"] - 1, r["eps"] / r["pred"],
               r["bound"] / abs(r["eps"]), r["pc"], r["split"]))

(OUT / "check_fall_full_grip.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
