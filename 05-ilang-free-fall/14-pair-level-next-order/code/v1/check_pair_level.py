"""Check of 14-pair-level-next-order: numerical diagonalization of the fibre contract H(P) of (11.1)
for a diagonal on-site binding, compared with the leading forms (11.14) and the next-order forms
(14.6)-(14.11). Also checks the effective operator (14.4) on a ring and the small-u forms (14.12).
Output: output/check_pair_level.log (all numbers cited in derivation.v1.md)."""
from pathlib import Path
import numpy as np

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)
LOG = []


def log(s=""):
    print(s)
    LOG.append(s)


# hatted data sets: (tau1, tau2, M1, M2, w11, w12, w21, w22); all w scale as eps^2, tau as eps
DATA = {
    "D1": (1.0, 1.6, 1.0, 2.5, -0.40, -0.50, 0.30, 0.70),
    "D2": (1.3, 0.8, 1.5, 0.7, +0.60, 0.40, -0.20, -0.50),
    "D3": (1.2, 0.9, 0.8, 1.3, -0.12, 0.20, 0.10, 0.30),
}
EPS = [0.2, 0.1, 0.05]
ETA = 0.5
H_FD = 0.05                      # finite-difference step in P (7-point stencil); 2*H_FD as control
P_LIST = [0.0, H_FD, 2 * H_FD, 3 * H_FD, 4 * H_FD, 6 * H_FD]


def fibre_sector(P, L, t1, t2, M1, M2, W, eta=ETA):
    """H(P) of (11.1) on r in [-L, L], restricted to the sector Theta = (-1)^r s3(1) s3(2) = +1."""
    sig3 = (1, -1)                                   # branch index 0 = branch 1 (upper), 1 = branch 2
    states = [(r, s1, s2) for r in range(-L, L + 1) for s1 in (0, 1) for s2 in (0, 1)
              if (-1) ** (r % 2) * sig3[s1] * sig3[s2] == 1]
    idx = {st: k for k, st in enumerate(states)}
    n = len(states)
    H = np.zeros((n, n), complex)
    e1p, e1m = np.exp(1j * eta * P), np.exp(-1j * eta * P)
    e2p, e2m = np.exp(1j * (1 - eta) * P), np.exp(-1j * (1 - eta) * P)
    for (r, s1, s2), k in idx.items():
        H[k, k] += M1 * sig3[s1] + M2 * sig3[s2] + (W[s1][s2] if r == 0 else 0.0)
        # A1 = (i t1/2) sigma1^(1) (e^{i eta P} S^dag - e^{-i eta P} S); (S^dag psi)(r) = psi(r+1)
        for rr, c in ((r + 1, 0.5j * t1 * e1p), (r - 1, -0.5j * t1 * e1m)):
            k2 = idx.get((rr, 1 - s1, s2))
            if k2 is not None:
                H[k, k2] += c
        # A2 = (i t2/2) sigma1^(2) (e^{i(1-eta)P} S - e^{-i(1-eta)P} S^dag); (S psi)(r) = psi(r-1)
        for rr, c in ((r - 1, 0.5j * t2 * e2p), (r + 1, -0.5j * t2 * e2m)):
            k2 = idx.get((rr, s1, 1 - s2))
            if k2 is not None:
                H[k, k2] += c
    s3a = np.array([sig3[s1] for (_, s1, _) in states], float)
    s3b = np.array([sig3[s2] for (_, _, s2) in states], float)
    return H, s3a, s3b


def bound_level(P, L, t1, t2, M1, M2, W, vec=False):
    H, s3a, s3b = fibre_sector(P, L, t1, t2, M1, M2, W)
    E0 = M1 + M2
    ev, U = np.linalg.eigh(H)
    top = np.where(ev > E0 - min(M1, M2))[0]          # cluster of the band B_++ and its bound level
    k = top[-1] if W[0][0] > 0 else top[0]
    if not vec:
        return ev[k]
    v = U[:, k]
    return ev[k], float(np.vdot(v, s3a * v).real), float(np.vdot(v, s3b * v).real)


def predictions(t1, t2, M1, M2, w):
    """Leading (11.14) and next-order (14.7)-(14.11) forms; unhatted inputs."""
    a1, a2 = t1 ** 2 / (4 * M1), t2 ** 2 / (4 * M2)
    a, b1, b2 = a1 + a2, a1 / M1, a2 / M2
    beta, sg, u = b1 + b2, np.sign(w), abs(w) / (a1 + a2)
    sig, nu = np.sqrt(1 + u * u), a1 * a2 / (a1 + a2) ** 2
    gs, gc, gm = a1 ** 2 / M1 + a2 ** 2 / M2, a2 ** 2 / M1 + a1 ** 2 / M2, a1 * a2 * (1 / M1 + 1 / M2)
    Lam = 1 + sg / sig
    sps = u * u / (sig + 1) if sg < 0 else sig + 1      # sig + sg, without cancellation for small u
    phA = 2 * sps / sig - u ** 2 + u ** 3 / sig
    phB = u ** 2 * (sg + sig - u) / sig
    dphA = -2 * u + 3 * u ** 2 / sig - u * (2 * sg + u ** 3) / sig ** 3
    dphB = 2 * u - 3 * u ** 2 / sig + (sg * u * (2 + u ** 2) + u ** 4) / sig ** 3
    E4 = -gs / 2 * phA - (gs + gm) / 2 * phB
    C = (2 * u ** 2 / sig ** 3 * (gs * (sg + sig ** 3 - u - u ** 3) - gm * (sg + sig ** 3 - 2 * u - u ** 3))
         + 4 * gm * (1 + sg / sig - 2 * u ** 2 + 2 * u ** 3 / sig) + 2 * u ** 2 * (sig - u) / sig * (gc + gm))
    Xi = [1.5 * bi * phA - gs / (2 * a) * u * dphA + 0.5 * (beta + 2 * a / Mi) * phB - beta / 2 * u * dphB
          for bi, Mi in ((b1, M1), (b2, M2))]
    Eb0, Epp0 = a * (1 + sg * sig), -4 * sg * nu * a / sig
    return dict(u=u, Eb0=Eb0, Eb1=Eb0 + E4, Epp0=Epp0, Epp1=Epp0 + nu * C,
                s30=[1 - b1 * Lam, 1 - b2 * Lam], s31=[1 - b1 * Lam + b1 * Xi[0], 1 - b2 * Lam + b2 * Xi[1]],
                mb0=1 / Epp0, mb1=(1 / Epp0) * (1 + sg * sig * C / (4 * a)),
                D=-(sig ** 2 * C - 4 * E4) / (16 * a1 * a2), E4=E4, nuC=nu * C, Xi=Xi, b=(b1, b2),
                gs=gs, gc=gc, gm=gm, a=a, a1=a1, a2=a2)


def Eb_closed(P, t1, t2, M1, M2, w):
    """E_b(P) - (M1+M2) of (14.6): leading part and order-eps^4 part."""
    a1, a2 = t1 ** 2 / (4 * M1), t2 ** 2 / (4 * M2)
    b1, b2 = a1 / M1, a2 / M2
    c2, c4 = np.cos(2 * P), np.cos(4 * P)
    s = np.sqrt(w * w + a1 ** 2 + a2 ** 2 + 2 * a1 * a2 * c2)
    aw, sg = abs(w), np.sign(w)
    k1, k2 = a1 + a2 * c2, a2 + a1 * c2
    l1, l2 = a1 ** 2 + 2 * a1 * a2 * c2 + a2 ** 2 * c4, a2 ** 2 + 2 * a1 * a2 * c2 + a1 ** 2 * c4
    g = (s + 2 * aw) / (s * (s + aw) ** 2)
    lead = a1 + a2 + sg * s
    corr = (-(a1 * b1 / 8) * (6 + 8 * sg * k1 / s + 2 * g * l1) - (a2 * b2 / 8) * (6 + 8 * sg * k2 / s + 2 * g * l2)
            - w * w / (2 * s) * (sg * (b1 + b2) + (b1 * k1 + b2 * k2) / (s + aw)))
    return lead, corr


def d2_7pt(f, h):
    """second derivative at 0 of an even function from f(0), f(h), f(2h), f(3h)"""
    return (4 * f[3] - 54 * f[2] + 540 * f[1] - 490 * f[0]) / (180 * h * h)


def slope(dev, eps):
    return [np.log(abs(dev[k] / dev[k + 1])) / np.log(eps[k] / eps[k + 1]) for k in range(len(dev) - 1)]


# ---------------------------------------------------------------- Part A: bound level of H(P)
log("Part A: bound level of H(P) (11.1), sector Theta=+1, open chain r in [-L, L], eta = %.2f" % ETA)
log("FD: 7-point stencil for E_b''(0), step h = %.3f; control step 2h = %.3f" % (H_FD, 2 * H_FD))
summary = {}
for name, (T1, T2, M1, M2, W11, W12, W21, W22) in DATA.items():
    a_hat = T1 ** 2 / (4 * M1) + T2 ** 2 / (4 * M2)
    u = abs(W11) / a_hat
    rho = np.sqrt(1 + u * u) - u
    L = 2 * int(np.ceil(40 / np.log(1 / rho)))          # |psi(L)| ~ rho^(L/2) <= e^-40
    log("")
    log("%s: tau^=(%.2f,%.2f) M=(%.2f,%.2f) w^=(w11 %.2f, w12 %.2f, w21 %.2f, w22 %.2f)  u=%.4f  L=%d"
        % (name, T1, T2, M1, M2, W11, W12, W21, W22, u, L))
    rows = []
    for eps in EPS:
        t1, t2, w = eps * T1, eps * T2, eps ** 2 * W11
        W = [[eps ** 2 * W11, eps ** 2 * W12], [eps ** 2 * W21, eps ** 2 * W22]]
        res = {}
        for LL in (L, int(1.5 * L)):
            E = []
            for P in P_LIST:
                if P == 0.0:
                    e, s1, s2 = bound_level(P, LL, t1, t2, M1, M2, W, vec=True)
                else:
                    e = bound_level(P, LL, t1, t2, M1, M2, W)
                E.append(e - (M1 + M2))
            Epp_h = d2_7pt([E[0], E[1], E[2], E[3]], H_FD)
            Epp_2h = d2_7pt([E[0], E[2], E[4], E[5]], 2 * H_FD)
            res[LL] = dict(Eb=E[0], Epp=Epp_h, Epp2h=Epp_2h, s3=(s1, s2), E03=E[5])
        r0, r1 = res[L], res[int(1.5 * L)]
        conv = max(abs(r0["Eb"] - r1["Eb"]), abs(r0["Epp"] - r1["Epp"]),
                   abs(r0["s3"][0] - r1["s3"][0]), abs(r0["s3"][1] - r1["s3"][1]))
        pr = predictions(t1, t2, M1, M2, w)
        lead03, corr03 = Eb_closed(0.3, t1, t2, M1, M2, w)
        row = dict(eps=eps, Eb=r0["Eb"], Epp=r0["Epp"], s3=r0["s3"], pr=pr, conv=conv,
                   fd=abs(r0["Epp"] - r0["Epp2h"]), E03=r0["E03"], E03p=(lead03, lead03 + corr03))
        rows.append(row)
        log("  eps=%.3f  E_bind=%.12e  E''(0)=%.12e  <s3_1>-1=%.6e  <s3_2>-1=%.6e" %
            (eps, row["Eb"], row["Epp"], row["s3"][0] - 1, row["s3"][1] - 1))
        log("            |change L->1.5L| max=%.1e   |E''(h)-E''(2h)|=%.1e" % (conv, row["fd"]))
    summary[name] = rows
    # deviations
    log("  deviation from leading form (11.14) | from next-order form (14.6)-(14.9); slopes in eps:")
    for lab, num, p0, p1 in (
            ("E_bind", lambda r: r["Eb"], lambda r: r["pr"]["Eb0"], lambda r: r["pr"]["Eb1"]),
            ("E''(0)", lambda r: r["Epp"], lambda r: r["pr"]["Epp0"], lambda r: r["pr"]["Epp1"]),
            ("<s3_1>", lambda r: r["s3"][0], lambda r: r["pr"]["s30"][0], lambda r: r["pr"]["s31"][0]),
            ("<s3_2>", lambda r: r["s3"][1], lambda r: r["pr"]["s30"][1], lambda r: r["pr"]["s31"][1]),
            ("E_b(0.3)", lambda r: r["E03"], lambda r: r["E03p"][0], lambda r: r["E03p"][1])):
        d0 = [num(r) - p0(r) for r in rows]
        d1 = [num(r) - p1(r) for r in rows]
        log("    %-8s lead: %s  slopes %s" % (lab, " ".join("%+.3e" % x for x in d0),
                                              " ".join("%.2f" % s for s in slope(d0, EPS))))
        log("    %-8s next: %s  slopes %s" % ("", " ".join("%+.3e" % x for x in d1),
                                              " ".join("%.2f" % s for s in slope(d1, EPS))))
    # item 3: m_b - (m1 + m2 - 4 m1 m2 E_bind)
    log("  item 3: D = m_b - (m1+m2-4 m1 m2 E_bind), numerical vs (14.11), both divided by m_b^(0):")
    for r in rows:
        eps = r["eps"]
        m1, m2 = M1 / (eps * T1) ** 2, M2 / (eps * T2) ** 2
        Dn = 1 / r["Epp"] - (m1 + m2 - 4 * m1 * m2 * r["Eb"])
        log("    eps=%.3f  D_num/m_b0=%+.6e  D_pred/m_b0=%+.6e  difference=%+.2e" %
            (eps, Dn / r["pr"]["mb0"], r["pr"]["D"] / r["pr"]["mb0"], (Dn - r["pr"]["D"]) / r["pr"]["mb0"]))
    log("  relative correction of m_b: numerical m_b/m_b^(0)-1 vs (14.10):")
    for r in rows:
        log("    eps=%.3f  num=%+.6e  pred=%+.6e" % (r["eps"], (1 / r["Epp"]) / r["pr"]["mb0"] - 1,
                                                    r["pr"]["mb1"] / r["pr"]["mb0"] - 1))

# ---------------------------------------------------------------- Part B: effective operator on a ring
log("")
log("Part B: spectrum of the B_++ cluster of H(P) on a ring of N_r = 40 sites vs the effective operator")
log("        (14.4) built from its explicit coefficients; P = 0.37, eta = 0.3, data D1")
NR, PB, EB = 40, 0.37, 0.3


def ring_full(P, t1, t2, M1, M2, W, eta):
    S = np.roll(np.eye(NR), 1, axis=0)                 # (S psi)(r) = psi(r-1)
    Sd = S.T
    T1 = 0.5j * t1 * (np.exp(1j * eta * P) * Sd - np.exp(-1j * eta * P) * S)
    T2 = 0.5j * t2 * (np.exp(1j * (1 - eta) * P) * S - np.exp(-1j * (1 - eta) * P) * Sd)
    s1, s3, I2 = np.array([[0, 1], [1, 0]]), np.diag([1.0, -1.0]), np.eye(2)
    P0 = np.zeros((NR, NR)); P0[0, 0] = 1
    H = (np.kron(T1, np.kron(s1, I2)) + np.kron(T2, np.kron(I2, s1)) + M1 * np.kron(np.eye(NR), np.kron(s3, I2))
         + M2 * np.kron(np.eye(NR), np.kron(I2, s3)) + np.kron(P0, np.diag([W[0][0], W[0][1], W[1][0], W[1][1]])))
    return np.linalg.eigvalsh(H)


def ring_eff(P, t1, t2, M1, M2, W, eta, order):
    a1, a2 = t1 ** 2 / (4 * M1), t2 ** 2 / (4 * M2)
    b1, b2 = a1 / M1, a2 / M2
    f1, f2 = np.exp(2j * eta * P), np.exp(-2j * (1 - eta) * P)
    w = W[0][0]
    H = np.zeros((NR, NR), complex)
    if order == 2:                                     # (11.11)
        diag, J2, J4, Jb, Om, Lc = a1 + a2, a1 * f1 + a2 * f2, 0, 0, 0, 0
    else:                                              # (14.4); order 3: without the w12, w21 terms
        diag = a1 * (1 - 0.75 * b1) + a2 * (1 - 0.75 * b2)
        J2 = a1 * (1 - b1) * f1 + a2 * (1 - b2) * f2
        J4 = a1 * b1 * f1 ** 2 + a2 * b2 * f2 ** 2
        Jb = b1 * f1 + b2 * f2
        Om = W[1][0] * b1 + W[0][1] * b2 if order == 4 else 0
        Lc = W[1][0] * b1 * f1 + W[0][1] * b2 * f2 if order == 4 else 0
    for r in range(NR):
        H[r, r] += M1 + M2 + diag
        H[r, (r + 2) % NR] += -0.5 * J2
        H[r, (r - 2) % NR] += -0.5 * np.conj(J2)
        H[r, (r + 4) % NR] += -0.125 * J4
        H[r, (r - 4) % NR] += -0.125 * np.conj(J4)
    beta = b1 + b2 if order > 2 else 0
    H[0, 0] += w * (1 - beta / 2)
    H[0, 2] += w / 8 * Jb; H[0, NR - 2] += w / 8 * np.conj(Jb)
    H[NR - 2, 0] += w / 8 * Jb; H[2, 0] += w / 8 * np.conj(Jb)
    H[1, 1] += Om / 4; H[NR - 1, NR - 1] += Om / 4
    H[NR - 1, 1] += -0.25 * Lc; H[1, NR - 1] += -0.25 * np.conj(Lc)
    assert np.allclose(H, H.conj().T)
    return np.linalg.eigvalsh(H)


T1, T2, M1, M2, W11, W12, W21, W22 = DATA["D1"]
devs = {2: [], 3: [], 4: []}
for eps in EPS:
    W = [[eps ** 2 * W11, eps ** 2 * W12], [eps ** 2 * W21, eps ** 2 * W22]]
    ev = ring_full(PB, eps * T1, eps * T2, M1, M2, W, EB)
    clus = np.sort(ev[ev > M1 + M2 - min(M1, M2)])
    for o in (2, 3, 4):
        devs[o].append(np.max(np.abs(clus - ring_eff(PB, eps * T1, eps * T2, M1, M2, W, EB, o))))
for o, lab in ((2, "(11.11)               "), (3, "(14.4) without w12,w21"),
               (4, "(14.4) complete       ")):
    log("  max |eigenvalue difference|, %s: %s  slopes %s" %
        (lab, " ".join("%.3e" % x for x in devs[o]), " ".join("%.2f" % s for s in slope(devs[o], EPS))))

# ---------------------------------------------------------------- Part C: small-u forms (14.12)
log("")
log("Part C: ordered limit u -> 0 (w11 < 0) of the eps^4 coefficients (hatted data of D3 and equal data);")
log("        ratio closed form / leading small-u term (14.12); u^4 term used where the u^3 term vanishes")
for lab, (T1, T2, M1, M2) in (("D3", DATA["D3"][:4]), ("equal", (1.0, 1.0, 1.0, 1.0))):
    a1, a2 = T1 ** 2 / (4 * M1), T2 ** 2 / (4 * M2)
    for u in (1e-2, 1e-3):
        p = predictions(T1, T2, M1, M2, -u * (a1 + a2))
        a, gs, gc, gm, nu = p["a"], p["gs"], p["gc"], p["gm"], a1 * a2 / (a1 + a2) ** 2
        lE = gm / 2 * u ** 3
        lC = 2 * nu * (gc - 2 * gm) * u ** 2
        lm = -(gc - 2 * gm) / (2 * a) * u ** 2
        out = ["E4 %.6f" % (p["E4"] / lE), "nuC %.6f" % (p["nuC"] / lC),
               "r_m %.6f" % ((p["mb1"] / p["mb0"] - 1) / lm)]
        for i, (ai, aj, Mi, Mj) in enumerate(((a1, a2, M1, M2), (a2, a1, M2, M1))):
            X3 = aj / (2 * a) * ((ai - 2 * aj) / Mi + (2 * ai - aj) / Mj)
            X4 = (ai ** 2 - 7 * ai * aj + 4 * aj ** 2) / (8 * a * Mi) + 3 * aj * (aj - ai) / (4 * a * Mj)
            lead = X3 * u ** 3 if abs(X3) > 1e-14 else X4 * u ** 4
            out.append("Xi_%d %.6f%s" % (i + 1, p["Xi"][i] / lead, "" if abs(X3) > 1e-14 else " (u^4)"))
        log("  %-5s u=%.0e: %s" % (lab, u, "  ".join(out)))

(OUT / "check_pair_level.log").write_text("\n".join(LOG) + "\n", encoding="utf-8")
