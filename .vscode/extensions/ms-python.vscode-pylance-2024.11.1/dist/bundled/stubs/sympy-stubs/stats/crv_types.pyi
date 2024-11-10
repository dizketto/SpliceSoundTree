from typing import Any
from typing_extensions import Self

from sympy import Equality, FiniteSet, Integral, Interval, Ne, Piecewise, Sum
from sympy.core.basic import Basic
from sympy.core.relational import Relational
from sympy.matrices import MatrixBase
from sympy.stats.crv import SingleContinuousDistribution
from sympy.stats.joint_rv import JointRandomSymbol
from sympy.stats.rv import RandomSymbol, is_random

oo = ...
__all__ = [
    "ContinuousRV",
    "Arcsin",
    "Benini",
    "Beta",
    "BetaNoncentral",
    "BetaPrime",
    "BoundedPareto",
    "Cauchy",
    "Chi",
    "ChiNoncentral",
    "ChiSquared",
    "Dagum",
    "Erlang",
    "ExGaussian",
    "Exponential",
    "ExponentialPower",
    "FDistribution",
    "FisherZ",
    "Frechet",
    "Gamma",
    "GammaInverse",
    "Gompertz",
    "Gumbel",
    "Kumaraswamy",
    "Laplace",
    "Levy",
    "LogCauchy",
    "Logistic",
    "LogLogistic",
    "LogitNormal",
    "LogNormal",
    "Lomax",
    "Maxwell",
    "Moyal",
    "Nakagami",
    "Normal",
    "GaussianInverse",
    "Pareto",
    "PowerFunction",
    "QuadraticU",
    "RaisedCosine",
    "Rayleigh",
    "Reciprocal",
    "StudentT",
    "ShiftedGompertz",
    "Trapezoidal",
    "Triangular",
    "Uniform",
    "UniformSum",
    "VonMises",
    "Wald",
    "Weibull",
    "WignerSemicircle",
]

@is_random.register(MatrixBase)
def _(x) -> bool: ...
def rv(symbol, cls, args, **kwargs) -> RandomSymbol: ...

class ContinuousDistributionHandmade(SingleContinuousDistribution):
    _argnames = ...
    def __new__(cls, pdf, set=...) -> Self: ...
    @property
    def set(self) -> Basic: ...
    @staticmethod
    def check(pdf, set) -> None: ...

def ContinuousRV(symbol, density, set=..., **kwargs) -> RandomSymbol: ...

class ArcsinDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    def pdf(self, x): ...

def Arcsin(name, a=..., b=...) -> RandomSymbol: ...

class BeniniDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(alpha, beta, sigma) -> None: ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    def pdf(self, x): ...

def Benini(name, alpha, beta, sigma) -> RandomSymbol: ...

class BetaDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...

def Beta(name, alpha, beta) -> RandomSymbol: ...

class BetaNoncentralDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(alpha, beta, lamda) -> None: ...
    def pdf(self, x) -> Equality | Relational | Ne | Sum: ...

def BetaNoncentral(name, alpha, beta, lamda) -> RandomSymbol: ...

class BetaPrimeDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(alpha, beta) -> None: ...

    set = ...
    def pdf(self, x): ...

def BetaPrime(name, alpha, beta) -> RandomSymbol: ...

class BoundedParetoDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(alpha, left, right) -> None: ...
    def pdf(self, x): ...

def BoundedPareto(name, alpha, left, right) -> RandomSymbol: ...

class CauchyDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(x0, gamma) -> None: ...
    def pdf(self, x): ...

def Cauchy(name, x0, gamma) -> RandomSymbol: ...

class ChiDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(k) -> None: ...

    set = ...
    def pdf(self, x): ...

def Chi(name, k) -> RandomSymbol: ...

class ChiNoncentralDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(k, l) -> None: ...

    set = ...
    def pdf(self, x): ...

def ChiNoncentral(name, k, l) -> RandomSymbol: ...

class ChiSquaredDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(k) -> None: ...

    set = ...
    def pdf(self, x): ...

def ChiSquared(name, k) -> RandomSymbol: ...

class DagumDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(p, a, b) -> None: ...
    def pdf(self, x): ...

def Dagum(name, p, a, b) -> RandomSymbol: ...
def Erlang(name, k, l) -> RandomSymbol: ...

class ExGaussianDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mean, std, rate) -> None: ...
    def pdf(self, x): ...

def ExGaussian(name, mean, std, rate) -> RandomSymbol: ...

class ExponentialDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(rate) -> None: ...
    def pdf(self, x): ...

def Exponential(name, rate) -> RandomSymbol: ...

class ExponentialPowerDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, alpha, beta) -> None: ...
    def pdf(self, x): ...

def ExponentialPower(name, mu, alpha, beta) -> RandomSymbol: ...

class FDistributionDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(d1, d2) -> None: ...
    def pdf(self, x): ...

def FDistribution(name, d1, d2) -> RandomSymbol: ...

class FisherZDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(d1, d2) -> None: ...
    def pdf(self, x): ...

def FisherZ(name, d1, d2) -> RandomSymbol: ...

class FrechetDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a, s, m) -> None: ...
    def __new__(cls, a, s=..., m=...) -> Self: ...
    def pdf(self, x): ...

def Frechet(name, a, s=..., m=...) -> RandomSymbol: ...

class GammaDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(k, theta) -> None: ...
    def pdf(self, x): ...

def Gamma(name, k, theta) -> RandomSymbol: ...

class GammaInverseDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def GammaInverse(name, a, b) -> RandomSymbol: ...

class GumbelDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(beta, mu, minimum) -> None: ...
    def pdf(self, x) -> Piecewise: ...

def Gumbel(name, beta, mu, minimum=...) -> RandomSymbol: ...

class GompertzDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(b, eta) -> None: ...
    def pdf(self, x): ...

def Gompertz(name, b, eta) -> RandomSymbol: ...

class KumaraswamyDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def Kumaraswamy(name, a, b) -> RandomSymbol: ...

class LaplaceDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, b) -> None: ...
    def pdf(self, x): ...

def Laplace(name, mu, b) -> RandomSymbol | JointRandomSymbol: ...

class LevyDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(mu, c) -> None: ...
    def pdf(self, x): ...

def Levy(name, mu, c) -> RandomSymbol: ...

class LogCauchyDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, x): ...

def LogCauchy(name, mu, sigma) -> RandomSymbol: ...

class LogisticDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x): ...

def Logistic(name, mu, s) -> RandomSymbol: ...

class LogLogisticDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...
    def expectation(self, expr, var, **kwargs) -> Piecewise: ...

def LogLogistic(name, alpha, beta) -> RandomSymbol: ...

class LogitNormalDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x): ...

def LogitNormal(name, mu, s) -> RandomSymbol: ...

class LogNormalDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mean, std) -> None: ...
    def pdf(self, x): ...

def LogNormal(name, mean, std) -> RandomSymbol: ...

class LomaxDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(alpha, lamda) -> None: ...
    def pdf(self, x): ...

def Lomax(name, alpha, lamda) -> RandomSymbol: ...

class MaxwellDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(a) -> None: ...
    def pdf(self, x): ...

def Maxwell(name, a) -> RandomSymbol: ...

class MoyalDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(mu, sigma) -> None: ...
    def pdf(self, x): ...

def Moyal(name, mu, sigma) -> RandomSymbol: ...

class NakagamiDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, omega) -> None: ...
    def pdf(self, x): ...

def Nakagami(name, mu, omega) -> RandomSymbol: ...

class NormalDistribution(SingleContinuousDistribution):
    _argnames = ...
    @staticmethod
    def check(mean, std) -> None: ...
    def pdf(self, x): ...

def Normal(name, mean, std) -> RandomSymbol | JointRandomSymbol: ...

class GaussianInverseDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(mean, shape) -> None: ...
    def pdf(self, x): ...

def GaussianInverse(name, mean, shape) -> RandomSymbol: ...

Wald = ...

class ParetoDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(xm, alpha) -> None: ...
    def pdf(self, x): ...

def Pareto(name, xm, alpha) -> RandomSymbol: ...

class PowerFunctionDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(alpha, a, b) -> None: ...
    def pdf(self, x): ...

def PowerFunction(name, alpha, a, b) -> RandomSymbol: ...

class QuadraticUDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x) -> Piecewise: ...

def QuadraticU(name, a, b) -> RandomSymbol: ...

class RaisedCosineDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(mu, s) -> None: ...
    def pdf(self, x) -> Piecewise: ...

def RaisedCosine(name, mu, s) -> RandomSymbol: ...

class RayleighDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(sigma) -> None: ...
    def pdf(self, x): ...

def Rayleigh(name, sigma) -> RandomSymbol: ...

class ReciprocalDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(a, b) -> None: ...
    def pdf(self, x): ...

def Reciprocal(name, a, b) -> RandomSymbol: ...

class ShiftedGompertzDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(b, eta) -> None: ...
    def pdf(self, x): ...

def ShiftedGompertz(name, b, eta) -> RandomSymbol: ...

class StudentTDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(nu) -> None: ...
    def pdf(self, x): ...

def StudentT(name, nu) -> RandomSymbol: ...

class TrapezoidalDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(a, b, c, d) -> None: ...
    def pdf(self, x) -> Piecewise: ...

def Trapezoidal(name, a, b, c, d) -> RandomSymbol: ...

class TriangularDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(a, b, c) -> None: ...
    def pdf(self, x) -> Piecewise: ...

def Triangular(name, a, b, c) -> RandomSymbol: ...

class UniformDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(left, right) -> None: ...
    def pdf(self, x) -> Piecewise: ...
    def expectation(self, expr, var, **kwargs) -> Equality | Basic | Relational | Ne | Integral | Any: ...

def Uniform(name, left, right) -> RandomSymbol: ...

class UniformSumDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(n) -> None: ...
    def pdf(self, x): ...

def UniformSum(name, n) -> RandomSymbol: ...

class VonMisesDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(mu, k) -> None: ...
    def pdf(self, x): ...

def VonMises(name, mu, k) -> RandomSymbol: ...

class WeibullDistribution(SingleContinuousDistribution):
    _argnames = ...
    set = ...
    @staticmethod
    def check(alpha, beta) -> None: ...
    def pdf(self, x): ...

def Weibull(name, alpha, beta) -> RandomSymbol: ...

class WignerSemicircleDistribution(SingleContinuousDistribution):
    _argnames = ...
    @property
    def set(self) -> FiniteSet | Interval: ...
    @staticmethod
    def check(R) -> None: ...
    def pdf(self, x): ...

def WignerSemicircle(name, R) -> RandomSymbol: ...
