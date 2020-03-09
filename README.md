# Survey of Distributions

Looking at relationships between distributions through code

## Continuous Distributions
for now, the starting point is the normal in code and the gamma in theory, due to the point of reference the game serves for other distributions.

### normal distribution
two parameters
- mean (location parameter)
- variance (scale parameter)

### gamma distribution and special cases
two parameters
- shape (`k`, positive real numbers)
- scale (`θ`, positive real numbers, `β` the inverse scale can also be used where `β=1/θ`)

known as maximum entropy distribution
for processes with waiting times between events... like the wating time between poisson distributed events

gamma function:
`Γ(k) = (k − 1)!`

##### Erlang is a case of Gamma
two parameters
- shape (positive **integer** know as `k`)
- rate (positive real number `λ`, 'scale' - reciprocal of rate can also be used)

the sum of `k` independent exponentially distributed random variables with mean `θ`
thought of as probability distribution of waiting time until `k-th` arrival.

##### exponential distribution
can be thought of multiple ways

- as an Erlang distribution with the shape parameter `k=1`
  - by extension, as a gamma distribution
- as the probability distribution of time between events of a poisson distribution
- backwards, `n` independent and identically distributed  exponential distributions random variables  sum to a gammma distribution with shape `n` and rate `λ`

##### chi-squared distribution
chi-squared is also a special case of the gamma distribution with `ν` degrees of freedom, where gamma(ν/2 ,2) = to χ2(ν)

##### normal distribution
for large `k` the gamma distribution converges to the normal distribution

##### cauchy distribution
two independent standard normal divided by one another


### dirichlet distribution
multivariate generalization of beta distribution

#### beta distribution
is a gamma distribution divided by the sum of that gamma distribution with another.
 a gamma(1) / (gamma(1) + gamma(2))

## Discrete Distributions
starting with the negative binomial distribution, due to relationship with gamma


### negative binomial
number of successes in a sequence of independent and identically distributed (iid) Bernoulli trials before `r` failures

can view the negative binomial as poisson distribution with `λ` being a random variable with a gamma distribution with shape `r` and scale `θ = p/(1-p)`

under certain paramters the negative binomial converges to the poisson


Sources

[wiki list of distribitions](https://en.wikipedia.org/wiki/List_of_probability_distributions)
