"""Check script of 08-ilang-propagation/06-mark-inertia, derivation v1.

Part A (check required by the question): ring of L = 32 cells. For a square grip
and one other grip of class (G2), two clock levels, both branches and
r = tau/c0 in {0.5, 1, 1.5}: the second-order coefficients (in delta F) of
Cost_{k,sigma} and of E''_{k,sigma}(0) from the formula (6.2), (6.3), (6.5) of the
derivation are compared with an independent computation: exact diagonalisation
of the total contract restricted to states with at most two field quanta, in the
sector of the joint label P (P continued continuously, E'' from the exact second
derivative of the eigenvalue), the second-order coefficient being extracted from
several small values of the scale s of delta F.

Part B: the formula (6.3) on long rings (L = 8 ell): rho = I^mark tau^2 / C^mark
of the one-quantum (F1^2) and two-quantum (F2^2) parts against 2 - r^2, and the
held mark against its leading form in ell, as ell grows.

Units: c0 = sqrt(kappa_h) = 1, F0 = 1, so eps_k = F0 M_k = M_k.
"""
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


S1 = np.array([[0.0, 1.0], [1.0, 0.0]])
S3 = np.diag([1.0, -1.0])


def modes(L, c0, mh):
    q = 2 * np.pi * np.arange(L) / L
    Om = np.sqrt(mh**2 + 2 * c0**2 * (1 - np.cos(q)))
    return q, Om, 1.0 / (2 * L * Om)          # c_q^2 = 1/(2 L Omega_q)


def omega(p, tau, eps):
    return np.sqrt(eps**2 + (tau * np.sin(p))**2)


def theta(p, tau, eps):
    return np.arctan(tau * np.sin(p) / eps)


# ------------------------------------------------------------------ formula (6.3)
def mark_sums(P, sigma, tau, eps, q, Om, c2, chunk=256):
    """(S1, S2) with E^(2)(P) = -M_k^2 (F1^2 S1 + F2^2 S2)."""
    wP, tP = omega(P, tau, eps), theta(P, tau, eps)

    def S(E, Q, w):
        p = P - Q
        th = 0.5 * (tP + theta(p, tau, eps))
        wp = omega(p, tau, eps)
        return np.sum(w * (np.cos(th)**2 / (E + sigma * (wp - wP))
                           + np.sin(th)**2 / (E - sigma * (wp + wP))))

    s1 = S(Om, q, c2)
    s2 = 0.0
    for i in range(0, len(q), chunk):
        sl = slice(i, i + chunk)
        s2 += S(Om[sl, None] + Om[None, :], q[sl, None] + q[None, :],
                2 * c2[sl, None] * c2[None, :])
    return s1, s2


def curv(f, h=1e-2):
    """Second derivative at 0 of an even function, Richardson in h."""
    f0 = f(0.0)
    c = lambda hh: 2 * (f(hh) - f0) / hh**2
    return (4 * c(h) - c(2 * h)) / 3


def formula_second_order(sigma, tau, eps, Mk, F1, F2, q, Om, c2):
    """Second-order coefficients of Cost and E''(0): mark part (6.3) plus the
    second-order part of the zero-quantum level sigma*omega-bar (6.2)."""
    w0 = np.sum(c2)

    def E2(P):
        a, b = mark_sums(P, sigma, tau, eps, q, Om, c2)
        zq = sigma * (F2 * w0 * Mk)**2 * (tau * np.sin(P))**2 / (2 * omega(P, tau, eps)**3)
        return -Mk**2 * (F1**2 * a + F2**2 * b) + zq

    return E2(0.0), curv(E2)


# ------------------------------------------------------------------ exact diagonalisation
def field_ops(L, q, Om, c2):
    states = [()] + [(i,) for i in range(L)] + list(combinations_with_replacement(range(L), 2))
    idx = {s: i for i, s in enumerate(states)}
    n = len(states)
    A = np.zeros((n, n))                       # sum_q c_q a_q on <= 2 quanta
    cq = np.sqrt(c2)
    for j, s in enumerate(states):
        for m in set(s):
            t = list(s)
            t.remove(m)
            A[idx[tuple(t)], j] += cq[m] * np.sqrt(s.count(m))
    Ef = np.array([Om[list(s)].sum() if s else 0.0 for s in states])
    Qn = np.array([q[list(s)].sum() if s else 0.0 for s in states])
    q0 = A + A.T                                # q at the body's cell (x = 0)
    nq2 = A @ A + A.T @ A.T + 2 * A.T @ A       # :q0^2:, exact on <= 2 quanta
    return Ef, Qn, q0, nq2, np.sum(c2)


def ed_levels(P, tau, eps, Mk, F1, F2, s, ops):
    Ef, Qn, q0, nq2, w0 = ops
    n = len(Ef)
    sn, cs = np.sin(P - Qn), np.cos(P - Qn)
    H = (np.kron(np.diag(Ef), np.eye(2)) + eps * np.kron(np.eye(n), S3)
         - tau * np.kron(np.diag(sn), S1)
         + s * Mk * np.kron(F1 * q0 + F2 * (nq2 + w0 * np.eye(n)), S3))
    H1 = -tau * np.kron(np.diag(cs), S1)        # dH/dP
    H2 = tau * np.kron(np.diag(sn), S1)         # d2H/dP2
    E, V = np.linalg.eigh(H)
    _, u0 = np.linalg.eigh(-tau * np.sin(P) * S1 + eps * S3)
    out = {}
    for sigma, col in ((+1, 1), (-1, 0)):
        ref = np.zeros(2 * n)
        ref[:2] = u0[:, col]                     # field vacuum x band sigma
        j = int(np.argmax(np.abs(V.T @ ref)))
        psi = V[:, j]
        d1 = V.T @ (H1 @ psi)
        m = np.arange(len(E)) != j
        Epp = psi @ H2 @ psi + 2 * np.sum(d1[m]**2 / (E[j] - E[m]))
        out[sigma] = (E[j], Epp)
    return out


def coeffs(svals, fpos, fneg, f0):
    """Fit even part s^2 a2 + s^4 a4 + s^6 a6 and odd part s a1 + s^3 a3 + s^5 a5."""
    s = np.array(svals)
    even = (np.array(fpos) + np.array(fneg)) / 2 - f0
    odd = (np.array(fpos) - np.array(fneg)) / 2
    a2 = np.linalg.solve(np.vstack([s**2, s**4, s**6]).T, even)[0]
    a1 = np.linalg.solve(np.vstack([s, s**3, s**5]).T, odd)[0]
    return a1, a2


def part_a():
    L, c0, mh = 32, 1.0, 0.25
    q, Om, c2 = modes(L, c0, mh)
    w0 = np.sum(c2)
    log(f"PART A: ring L={L}, c0={c0}, m_h={mh} (ell={c0/mh}), F0=1, "
        f"G0={2*np.sum(c2/Om):.6f}, w0={w0:.6f}, Omega_max={Om.max():.4f}")
    log("second-order coefficients: formula (6.2), (6.3), (6.5) vs ED restricted to <= 2 quanta")
    ops = field_ops(L, q, Om, c2)
    grips = {"square (F1=0.3, F2=F1^2/4=0.0225)": (0.3, 0.0225),
             "other  (F1=0.3, F2=-0.15)": (0.3, -0.15)}
    svals = [0.01, 0.02, 0.04]
    maxrel = 0.0
    log(f"{'grip':36s} {'Mk':>3s} {'sig':>3s} {'r':>4s} | {'Cost2 form':>12s} {'Cost2 ED':>12s}"
        f" | {'E2pp form':>12s} {'E2pp ED':>12s} | {'Cost1 ED-form':>13s} {'Epp1 ED-form':>13s}")
    for gname, (F1, F2) in grips.items():
        for Mk in (3.0, 4.0):
            eps = Mk
            for r in (0.5, 1.0, 1.5):
                tau = r * c0
                res = {sv: ed_levels(0.0, tau, eps, Mk, F1, F2, sv, ops)
                       for sv in [0.0] + svals + [-x for x in svals]}
                for sigma in (+1, -1):
                    e0, p0 = res[0.0][sigma]
                    c1, c2c = coeffs(svals, [res[x][sigma][0] for x in svals],
                                     [res[-x][sigma][0] for x in svals], e0)
                    d1, d2 = coeffs(svals, [res[x][sigma][1] for x in svals],
                                    [res[-x][sigma][1] for x in svals], p0)
                    fc, fpp = formula_second_order(sigma, tau, eps, Mk, F1, F2, q, Om, c2)
                    c1f = sigma * Mk * F2 * w0
                    d1f = -sigma * tau**2 * F2 * w0 / Mk
                    rel = max(abs(c2c - fc) / abs(fc), abs(d2 - fpp) / abs(fpp))
                    maxrel = max(maxrel, rel)
                    log(f"{gname:36s} {Mk:3.0f} {sigma:+3d} {r:4.1f} | {fc:12.8f} {c2c:12.8f}"
                        f" | {fpp:12.8f} {d2:12.8f} | {c1-c1f:13.2e} {d1-d1f:13.2e}")
                    # zeroth order: bare level and curvature of (6.7) of 04-ilang-time/06-inertia-internal-energy
                    assert abs(e0 - sigma * eps) < 1e-10
                    assert abs(p0 - sigma * tau**2 / eps) < 1e-8
    log(f"max relative deviation of second-order coefficients (formula vs ED): {maxrel:.2e}")
    log("zeroth order: ED level = sigma*F0*M_k and E''(0) = sigma*tau^2/(F0*M_k) asserted to 1e-10 / 1e-8")
    return maxrel


def part_b():
    c0 = 1.0
    log("")
    log("PART B: formula (6.3) on rings with L = 8 ell, c0 = 1, F0 = 1;")
    log("rho_1, rho_2 = I^mark tau^2/C^mark of the F1^2 and F2^2 parts; prediction (6.9): 2 - r^2")
    log("held mark: g1 = G0*2c0^2/ell, g2 = J2*16c0^3/ell (prediction (6.7): -> 1);"
        " Cratio = C^mark(tau)/C^mark(0) for the F1^2 part")
    log("t_i = rho_i + 2 sigma eps_k R_i: rho with the term (iv) of Step 6 removed,"
        " R_i = <<sin^2 Q/E^2>>/<<1/E>> of the part i")
    log(f"{'ell':>5s} {'g1':>8s} {'g2':>8s} {'Mk':>3s} {'sig':>3s} {'r':>4s} {'2-r^2':>6s}"
        f" {'rho_1':>9s} {'rho_2':>9s} {'t_1':>9s} {'t_2':>9s} {'Cratio':>8s}")
    for ell in (16, 32, 64, 128, 256, 512):
        mh, L = c0 / ell, 8 * ell
        q, Om, c2 = modes(L, c0, mh)
        G0 = 2 * np.sum(c2 / Om)
        J2, N2 = 0.0, 0.0
        for i in range(0, L, 256):
            Es = Om[i:i+256, None] + Om[None, :]
            ww = c2[i:i+256, None] * c2[None, :]
            J2 += np.sum(ww / Es)
            N2 += np.sum(ww * np.sin(q[i:i+256, None] + q[None, :])**2 / Es**2)
        R1 = np.sum(c2 * np.sin(q)**2 / Om**2) / (G0 / 2)
        R2 = N2 / J2
        g1, g2 = G0 * 2 * c0**2 / ell, J2 * 16 * c0**3 / ell
        for Mk in (3.0, 4.0):
            eps = Mk
            for sigma in (+1, -1):
                for r in (0.5, 1.0, 1.5):
                    tau = r * c0
                    cache = {}

                    def ms(P):
                        if P not in cache:
                            cache[P] = mark_sums(P, sigma, tau, eps, q, Om, c2)
                        return cache[P]
                    C1, C2 = -Mk**2 * ms(0.0)[0], -Mk**2 * ms(0.0)[1]
                    E1 = -Mk**2 * curv(lambda P: ms(P)[0])
                    E2 = -Mk**2 * curv(lambda P: ms(P)[1])
                    I1, I2 = -(eps**2 / tau**4) * E1, -(eps**2 / tau**4) * E2
                    rho1, rho2 = I1 * tau**2 / C1, I2 * tau**2 / C2
                    cr = C1 / (-Mk**2 * G0 / 2)
                    t1, t2 = rho1 + 2 * sigma * eps * R1, rho2 + 2 * sigma * eps * R2
                    log(f"{ell:5d} {g1:8.5f} {g2:8.5f} {Mk:3.0f} {sigma:+3d} {r:4.1f} {2-r*r:6.2f}"
                        f" {rho1:9.5f} {rho2:9.5f} {t1:9.5f} {t2:9.5f} {cr:8.5f}")


if __name__ == "__main__":
    part_a()
    part_b()
    (OUT / "check_mark_inertia.txt").write_text("\n".join(LOG) + "\n", encoding="utf-8")
