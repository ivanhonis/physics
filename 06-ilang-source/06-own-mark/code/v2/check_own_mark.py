"""Check for 06-own-mark (derivation v2).

Exact diagonalization of the total contract in the sectors (k, P) for one field
object (N_f = 1) on rings of two sizes, for the couplings (a) and (c), three clock
levels and both branches.  Compared with the second-order results of the
derivation: dressed level E_{k,sigma}(0) (6.5)-(6.6), clock spacings (6.8), and
curvature E''_{k,sigma}(0) (6.10) with the leading-tau^2 forms (6.11), and the inertia-cost comparison (6.12).
The curvature of the exact level is the exact derivative of the eigenvalue of
the sector matrix C(P) (6.1) at P = 0 (second-order Hellmann-Feynman formula).
"""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(parents=True, exist_ok=True)

T_F, M_REST, D_C = 1.0, 3.0, 0.5   # t_f, m, clock spacing d_{k+1}-d_k = 2 pi/(N lambda_0)
LEVELS = [0, 1, 2]                  # clock levels k (N = 3)
RINGS = [6, 10]
TAUS = [1.0, 0.25]
GAMMAS = [0.01, 0.02, 0.04, 0.08]
N_F = 1
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)


def shift(L, d):                    # |r> -> |r+d>, r = x_f - x_b
    S = np.zeros((L, L))
    for r in range(L):
        S[(r + d) % L, r] = 1.0
    return S


def half_proj(L, rs):               # (1/2) sum_{r in rs} |r><r|
    P = np.zeros((L, L))
    for r in rs:
        P[r % L, r % L] += 0.5
    return P


def sector_parts(L, M, tau, g, coupling):
    """C(P) = C0 + e^{-iP} Am + e^{iP} Ap on branch (x) relative coordinate."""
    I2, Ir = np.eye(2), np.eye(L)
    Sp, Sm = shift(L, 1), shift(L, -1)
    n0 = np.zeros((L, L)); n0[0, 0] = 1.0
    C0 = M * np.kron(S3, Ir) - T_F * np.kron(I2, Sp + Sm) + g * M * np.kron(S3, n0)
    Am = 0.5 * tau * np.kron(-1j * S1, Sm)      # body x -> x+1
    Ap = 0.5 * tau * np.kron(1j * S1, Sp)       # body x+1 -> x
    if coupling == "c":                         # bond factor (Phi_x + Phi_{x+1})/2
        Am = Am + g * 0.5 * tau * np.kron(-1j * S1, Sm @ half_proj(L, [0, 1]))
        Ap = Ap + g * 0.5 * tau * np.kron(1j * S1, Sp @ half_proj(L, [-1, 0]))
    return C0, Am, Ap


def exact(L, M, tau, g, coupling, sigma):
    C0, Am, Ap = sector_parts(L, M, tau, g, coupling)
    C = C0 + Am + Ap
    assert np.allclose(C, C.conj().T)
    w, V = np.linalg.eigh(C)
    beta = np.array([1.0, 0.0]) if sigma > 0 else np.array([0.0, 1.0])
    v0 = np.kron(beta, np.ones(L) / np.sqrt(L))      # body (P=0, sigma), field lowest
    i = int(np.argmax(np.abs(V.conj().T @ v0)))
    psi, oth = V[:, i], np.arange(len(w)) != i
    a = V.conj().T @ ((-1j * Am + 1j * Ap) @ psi)
    curv = np.real(psi.conj() @ (-(Am + Ap)) @ psi) \
        + 2.0 * np.sum(np.abs(a[oth]) ** 2 / (w[i] - w[oth]))
    # sanity: finite difference of the analytic continuation C(P)
    h = 1e-3
    ev = [np.linalg.eigvalsh(C0 + np.exp(-1j * P) * Am + np.exp(1j * P) * Ap) for P in (-h, h)]
    fd = (ev[0][i] + ev[1][i] - 2 * w[i]) / h ** 2
    assert abs(fd - curv) < 1e-4 * max(1.0, abs(curv)), (fd, curv)
    return w[i], curv, float(np.min(np.abs(w[oth] - w[i])))


def G(P, q, M, tau, sigma, coupling):
    """Per-label second-order function G_{k,sigma}(P,q) of (6.5)."""
    Om = sigma * np.sqrt(M ** 2 + tau ** 2 * np.sin(P) ** 2 + 0j)
    sp, spp = np.sin(P), np.sin(P - q)
    eps = 2 * T_F * (1 - np.cos(q))
    z = Om - eps
    wp2 = M ** 2 + tau ** 2 * spp ** 2
    den = z ** 2 - wp2
    if coupling == "a":
        num = M ** 2 * (z + (M ** 2 - tau ** 2 * sp * spp) / Om)
    else:
        cp = (M ** 2 + tau ** 2 * sp * spp) / Om
        S = Om ** 2 + wp2
        num = (z * S + 2 * Om * wp2 + cp * (S + 2 * Om * z)) / 4
    return num / den


def d2_at0(f, r=0.1, n=64):        # exact second derivative of an analytic f at 0 (Cauchy)
    th = 2 * np.pi * np.arange(n) / n
    return float(np.real(2 * np.mean(f(r * np.exp(1j * th)) * np.exp(-2j * th)) / r ** 2))


def qs(L):
    return 2 * np.pi * np.arange(1, L) / L


def c2_energy(L, M, tau, sigma, coupling):          # gamma^2 coefficient of E(0), (6.5)
    n = N_F / L
    return n / L * sum(float(np.real(G(0.0, q, M, tau, sigma, coupling))) for q in qs(L))


def c2_energy_closed(L, M, tau, sigma, coupling):   # closed forms (6.6)
    n, Ms, tot = N_F / L, sigma * M, 0.0
    for q in qs(L):
        e, b2 = 2 * T_F * (1 - np.cos(q)), tau ** 2 * np.sin(q) ** 2
        K = e * (2 * Ms - e) + b2
        tot += -(M ** 2 * (2 * Ms - e) + (b2 * (Ms - e / 4) if coupling == "c" else 0.0)) / K
    return n / L * tot


def c2_curv(L, M, tau, sigma, coupling):            # gamma^2 coefficient of E''(0), (6.10)
    n = N_F / L
    return n / L * sum(d2_at0(lambda P: G(P, q, M, tau, sigma, coupling)) for q in qs(L))


def c2_curv_lead(L, M, tau, sigma, coupling):       # leading tau^2 forms (6.11)
    n, Ms, tot = N_F / L, sigma * M, 0.0
    for q in qs(L):
        c, e = np.cos(q), 2 * T_F * (1 - np.cos(q))
        if coupling == "a":
            tot += 2 * Ms * tau ** 2 * (1 + c) * (1 - Ms / T_F) / (e * (2 * Ms - e))
        else:
            tot += -tau ** 2 * (1 + c) * (2 * M ** 2 / T_F + 2 * Ms * (2 * c - 1) - e * c) / (e * (2 * Ms - e))
    return n / L * tot


def mf_curv(M, tau, g, sigma, coupling, L):         # mean-field part of (6.10), to gamma^2
    gn = g * N_F / L
    return sigma * tau ** 2 / M * ((1 - gn + gn ** 2) if coupling == "a" else (1 + gn))


def slope(xs, ys):
    return float(np.polyfit(np.log(xs), np.log(np.abs(ys)), 1)[0])


lines, rows = [], ["coupling,L,tau,k,sigma,gamma,E_exact,E_pred,dE,curv_exact,curv_pred,dcurv,gap"]
lines.append("Check of 06-own-mark v2: N_f=1, t_f=%.2f, m=%.2f, clock spacing=%.2f, levels k=%s"
             % (T_F, M_REST, D_C, LEVELS))
lines.append("Closed forms (6.6) vs general (6.5) at P=0, max abs difference of gamma^2 coefficients:")
mx = max(abs(c2_energy(L, M_REST + k * D_C, t, s, cp) - c2_energy_closed(L, M_REST + k * D_C, t, s, cp))
         for L in RINGS for t in TAUS for k in LEVELS for s in (1, -1) for cp in "ac")
lines.append("  %.2e" % mx)
lines.append("")
lines.append("A. Dressed level E(0) and curvature E''(0): deviation exact - second order, slope in gamma")
lines.append("   coupling L  tau   k sigma | dE(g=0.01)  dE(g=0.08)  slope | dE''(g=0.01) dE''(g=0.08) slope | min gap")
spac = {}
for cp in "ac":
    for L in RINGS:
        for tau in TAUS:
            for k in LEVELS:
                M = M_REST + k * D_C
                for s in (1, -1):
                    c2E, c2C = c2_energy(L, M, tau, s, cp), c2_curv(L, M, tau, s, cp)
                    dEs, dCs, gaps = [], [], []
                    for g in GAMMAS:
                        E, curv, gap = exact(L, M, tau, g, cp, s)
                        Ep = s * M * (1 + g * N_F / L) - 2 * T_F * N_F + g ** 2 * c2E
                        Cp = mf_curv(M, tau, g, s, cp, L) + g ** 2 * c2C
                        dEs.append(E - Ep); dCs.append(curv - Cp); gaps.append(gap)
                        rows.append("%s,%d,%.3f,%d,%d,%.3f,%.12f,%.12f,%.3e,%.12f,%.12f,%.3e,%.4f"
                                    % (cp, L, tau, k, s, g, E, Ep, E - Ep, curv, Cp, curv - Cp, gap))
                        if s > 0:
                            spac[(cp, L, tau, k, g)] = E
                    lines.append("   (%s)     %2d %.2f  %d  %+d   | %10.2e  %10.2e  %4.2f | %10.2e  %10.2e  %4.2f | %.3f"
                                 % (cp, L, tau, k, s, dEs[0], dEs[-1], slope(GAMMAS, dEs),
                                    dCs[0], dCs[-1], slope(GAMMAS, dCs), min(gaps)))
lines.append("")
lines.append("B. Clock spacings E_{k+1,+}(0)-E_{k,+}(0): exact - [(1+gamma n) spacing + gamma^2 (c2_{k+1}-c2_k)],")
lines.append("   slope in gamma; and the second-order change per unit spacing, (c2_{k+1}-c2_k)/spacing, for k=0,1")
for cp in "ac":
    for L in RINGS:
        for tau in TAUS:
            c2 = [c2_energy(L, M_REST + k * D_C, tau, 1, cp) for k in LEVELS]
            rel = [(c2[k + 1] - c2[k]) / D_C for k in LEVELS[:-1]]
            out = []
            for k in LEVELS[:-1]:
                devs = [spac[(cp, L, tau, k + 1, g)] - spac[(cp, L, tau, k, g)]
                        - ((1 + g * N_F / L) * D_C + g ** 2 * (c2[k + 1] - c2[k])) for g in GAMMAS]
                out.append("k=%d: dev(g=0.08)=%.2e slope %.2f" % (k, devs[-1], slope(GAMMAS, devs)))
            lines.append("   (%s) L=%2d tau=%.2f | %s | %s | change/spacing: k=0 %.5f, k=1 %.5f"
                         % (cp, L, tau, out[0], out[1], rel[0], rel[1]))
lines.append("")
lines.append("C. Leading-tau^2 curvature (6.11) vs full second-order curvature (6.10), relative deviation")
for cp in "ac":
    for L in RINGS:
        for s in (1, -1):
            devs = []
            for tau in (0.2, 0.1, 0.05):
                full, lead = c2_curv(L, M_REST, tau, s, cp), c2_curv_lead(L, M_REST, tau, s, cp)
                devs.append(abs(lead - full) / abs(full))
            lines.append("   (%s) L=%2d sigma=%+d k=0 | tau=0.2: %.2e  tau=0.1: %.2e  tau=0.05: %.2e"
                         % (cp, L, s, *devs))
lines.append("")
lines.append("D. Own mark (6.12): gamma^2 coefficients at P=0, sigma=+: cost c2E, curvature c2C,")
lines.append("   inertia change -(M^2/tau^4) c2C vs cost change / tau^2 = c2E/tau^2")
for cp in "ac":
    for L in RINGS:
        for tau in TAUS:
            for k in LEVELS:
                M = M_REST + k * D_C
                c2E, c2C = c2_energy(L, M, tau, 1, cp), c2_curv(L, M, tau, 1, cp)
                lines.append("   (%s) L=%2d tau=%.2f k=%d M=%.2f | c2E=%+.5f c2C=%+.6f | inertia %+.4f  cost/tau^2 %+.4f"
                             % (cp, L, tau, k, M, c2E, c2C, -M ** 2 / tau ** 4 * c2C, c2E / tau ** 2))

(OUT / "check_own_mark.log").write_text("\n".join(lines) + "\n", encoding="utf-8")
(OUT / "check_own_mark.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("\n".join(lines))
