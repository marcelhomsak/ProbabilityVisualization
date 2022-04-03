from math import e


# Factorial and binomial functions

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)


def binomial(n, r):
    return (fact(n)) // (fact(n - r) * fact(r))


# Functions return probability for a certain random variable x

def dbinom(k, n, p):
    return round(binomial(n, k) * p**k * (1-p)**(n-k), 8)


def dgeom(k, p):
    return round((1-p)**(k-1) * p, 8)


def dnbinom(k, n, p):
    return round(binomial(k-1, n-1) * (1-p)**(k-n) * p**n, 8)


def dhyper(k, r, b, n):
    return round((binomial(r, k) * binomial(b, (n-k))) / binomial((r+b), n), 8)


def dpois(k, lam):
    return round(((lam**k) / fact(k)) * e**(-lam), 8)


# Functions return the value of the probability density function (pdf) given a certain random variable x

def pbinom(k, n, p):
    return round(sum([dbinom(i, n, p) for i in range(k+1)]), 8)


def pgeom(k, p):
    return round(sum([dgeom(i, p) for i in range(1, k+1)]), 8)


def pnbinom(k, n, p):
    return round(sum([dnbinom(i, n, p) for i in range(n, k+1)]), 8)


def phyper(k, r, b, n):
    return None if k > min(n, r) else round(sum([dhyper(i, r, b, n) for i in range(k+1)]), 8)


def ppois(k, lam):
    return sum([dpois(i, lam) for i in range(k+1)])


# Functions return the expected value

def ebinom(n, p):
    return n * p


def egeom(p):
    return 1 / p


def enbinom(n, p):
    return n / p


def ehyper(r, b, n):
    return (n * r) / (r + b)


def epois(lam):
    return lam


# Schemes for distributions (dictionary -> key=X, value=probability)

def sbinom(n, p):
    return {i: dbinom(i, n, p) for i in range(n+1)}


def sgeom(p, last):
    return {i: dgeom(i, p) for i in range(1, last+1)}


def snbinom(n, p, last):
    return {i: dnbinom(i, n, p) for i in range(n, last+1)}


def shyper(r, b, n):
    return {i: dhyper(i, r, b, n) for i in range(min(n, r)+1)}


def spois(lam, last):
    return {i: dpois(i, lam) for i in range(last+1)}