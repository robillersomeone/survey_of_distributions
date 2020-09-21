# Survey of Distributions

looking at relationships between distributions.

the code for the site can be found [here](https://github.com/robillersomeone/robillersomeone.github.io).

typos are normally distributed, so if you see one please let me know.

## Continuous Distributions
the starting point is the gamma in theory and code in `distributions.py`, due to the point of reference the gamma serves for other distributions.

the graphing code can be found in the viz directory, all graphs are of the probability density function for the given distribution over a subset of their support, normally `[0, 20)`,`[0,1]`, or `[0,5]`.

### normal distribution
two parameters
- mean (`μ` location parameter)
- variance (`σ^2` scale parameter)


more later on...

### gamma distribution and special cases (Pearson type III)
two parameters
- shape (`k`, positive real numbers)
- scale (`θ`, positive real numbers, `β` the inverse scale - 'rate' can also be used where `β=1/θ`)

support : `(0,∞)`

known as maximum entropy distribution
for processes with waiting times between events... like the waiting time between poisson distributed events

two constructions
- using exponentials and the gamma function for positive integers:
`Γ(k) = (k − 1)!`
- using the improper integral from `[0,∞)` for complex numbers
    - this is used to build the distributions that follow

<img src="./imgs/gamma_distributions.png" height="300px" width="400px">

### erlang is a case of gamma
two parameters
- shape (`k` positive **integer**)
- rate (`λ` positive real number, 'scale' - reciprocal of rate (`1/λ`) can also be used)

support : `[0,∞)`

**in relation to gamma** it's the gamma distribution with the shape parameter as an integer

the sum of `k` independent exponentially distributed random variables with mean `θ`
thought of as probability distribution of waiting time until `k-th` arrival.

in relation to chi-squared, it's a chi-squared distribution with 2k degrees of freedom, when `scale=2` ~ generalized chi-squared distribution

the scale parameterization is implemented in `distributions.py` 

<img src="./imgs/erlang_distribution_9_1.png" height="300px" width="400px">

### exponential distribution (Pearson type III)
one parameter
- rate (`λ` over the interval ``[0,∞)``)

support : `[0,∞)`

**in relation to gamma**
- as an Erlang distribution with the shape parameter 'fixed' as `k=1`
  - the sum of `k` exponential distributions is an Erlang distribution with `(k,λ)`
  - by extension, as a gamma distribution
- as the probability distribution of time between events of a poisson distribution
- backwards, `n` independent and identically distributed  exponential distributions random variables  sum to a gamma distribution with shape `n` and rate `λ`

in relation to discrete distributions it's the continuous case of the geometric

has a memoryless property - past is not helpful in predicting the future.

<img src="./imgs/exponential_distribution_1.png" height="300px" width="400px">

### chi-squared distribution (Pearson type III)
one parameter
- degrees of freedom (`k`, the sum of the squared of independent standard normal distributions)

support : `[0,∞)`

**in relation to gamma** chi-squared is a special case of the gamma distribution with `ν` degrees of freedom, where `gamma(ν/2 ,2) = χ2(ν)`

used in hypothesis testing, as goodness of fit and independence.

<img src="./imgs/chi_squared_distribution_3.png" height="300px" width="400px">

### chi distribution
one parameter
- degrees of freedom (`k>0`)

support : `[0,∞)`

**in relation to gamma** square it to get the chi-squared distribution (which is a special case of the gamma distribution)

if `degrees of freedom=1` the chi distribution is a half normal distribution

if `degrees of freedom=2` the chi distribution is a rayleigh distribution

if `degrees of freedom=3` the chi distribution is a maxwell distribution

the absolute value of a standard normal distribution is a chi distribution

<img src="./imgs/chi_distribution.png" height="300px" width="400px">

### nakagami distribution
two parameters
- shape (`μ>=.5`)
- spread (`w>0`, can also use omega)

support : `x>0`

used to model wireless signals

**in relation to gamma** the square root of a gamma distribution is the nakagami distribution

nakagami distribution is the square root of a scaled chi distribution, this is generalization of the chi distribution.

nakagami distribution with `shape=1` is a rayleigh and a weibull distribution, also if `spread=2` it's an exponential distribution.

<img src="./imgs/nakagami_distribution.png" height="300px" width="400px">

### laplace distribution
two parameters
- location (`μ` real number)
- scale (`b` real number > 0)

support : real numbers (all of 'em)

**in relation to gamma** the laplace distribution is made from the difference of two exponentials (a special case of the erlang distribution, which is a case of the gamma distribution), because of this if we take the absolute value of one laplace distribution we get a chi-square distribution, and a f-distribution if we use two laplaces distributions.

in LASSO regression, is a bayesian regression with a laplace prior.

can be thought of a composite/double distribution

related to the normal distribution
  - normal - is the squared different from the mean
  - laplace - is the absolute difference from the mean

also, check out the laplace transform, which is neat.

from laplace - the frequency of an error is an exponential function of its magnitude without the sign

<img src="./imgs/laplace_distribution.png" height="300px" width="400px">

### logistic distribution
two parameters
- location (`μ`)
- scale (`s>0`)

support : `(-∞,∞)`

used in logistic regression!

**in relation to gamma** scaled log of the ratio of two exponential(1) distributions (which is a special case of the gamma distribution)

log of uniforms can get to the logistic distribution as well

the different of two gumbel distributions is a logistic distribution

<img src="./imgs/logistic_distribution.png" height="300px" width="400px">

### beta distribution (Pearson type I)
two parameters
- shape (`𝛼`)
- shape (`β`)

support : `[0,1]`, so good for probabilities

'distribution over distributions', defining binomial coefficient for continuous variables


**in relation to gamma** is a gamma distribution divided by the sum of that gamma distribution with another, which takes the form `gamma(1) / (gamma(1) + gamma(2))`

 the beta *function* is the product of two iid gamma functions divided by the sum of the two random variables in a gamma function.
 
 the multivariate beta distribution is the dirichlet distribution.
 
 the beta distribution is the conjugate to binomial distribution.

here the beta distribution is symmetric, the alpha and beta parameters are equal positive integers.

<img src="./imgs/beta_distributions_alpha_equals_beta.png" height="300px" width="400px">

here the beta distribution is symmetric, the alpha and beta parameters are equal real numbers less than one. 

<img src="./imgs/beta_distributions_alpha_equals_beta_fractions.png" height="300px" width="400px">

here the alpha parameter is greater than the beta parameter.

<img src="./imgs/beta_distr_alpha_greater.png" height="300px" width="400px">

here the beta parameter is greater than the alpha parameter.

<img src="./imgs/beta_distr_alpha_less.png" height="300px" width="400px">


### arcsine distribution

special case of beta distribution where `Beta(.5, .5)`

**in relation to gamma** it's a type of beta distribution, which is a ratio of gamma distributions.


<img src="./imgs/arcsin_distribution.png" height="300px" width="400px">

### uniform distribution

special case of beta distribution where `Beta(1, 1)`

**in relation to gamma** it's a type of beta distribution, which is a ratio of gamma distributions.

<img src="./imgs/uniform_distribution.png" height="300px" width="400px">

### kumaraswamy distribution
two parameters
- shape (`a>0`)
- shape (`b>0`)

support : (0,1)

**in relation to gamma** the negative log of the kumaraswamy(a,1) is the exponential(a)

also, is a special case of the beta distribution

kumaraswamy(1,1) is a uniform distribution

<img src="./imgs/kumaraswamy_distribution.png" height="300px" width="400px">

### beta prime distribution (pearson type VI)
two parameters
- shape (`𝛼`)
- shape (`β`)

support : `[0,∞)`

beta prime is the conjugate prior distribution of the bernoulli expressed in odds.

**in relation to gamma** it's the ratio of two gamma distributions, both with `scale=1`

the inverted dirichlet distribution is a generalization of the beta prime distribution

beta prime makes the log-logistic distribution

<img src="./imgs/beta_prime_distribution.png" height="300px" width="400px">

### dagum distribution
three parameters
- shape `p>0`
- shape `a>0`
- scale `b>0`

support : `x>0`

**in relation to gamma** the dagum distribution is a special case of the beta prime distribution

<img src="./imgs/dagum_distribution.png" height="300px" width="400px">

### f-distribution (Pearson type VI)
two parameters
- degrees of freedom in numerator (`n`, positive integer)
- degrees of freedom in denominator (`m`, positive integer)

support : `[0,∞)`, if `n=1` then `(0,∞)`

**in relation to gamma** f-distribution is the ratio of two chi squared distributions (where the chi-squared is a special case of the gamma distribution)

used to model ratio of sample variances, for Analysis Of Variance (ANOVA) and regression

f-distribution is also a specific parameterization of the beta prime distribution (inverted beta distribution)

used in f-test in hypothesis testing. null hypothesis ~ two independent normal variances are equal.

in the code, it's built with the gamma function tranforming the sums of the degrees of freedom as well as the individual degrees of freedom - all divided by 2, the f-distribution can be thought of as two the chi-squared parameterizations of the gamma distribution.

<img src="./imgs/f_distributions.png" height="300px" width="400px">

### normal distribution
two parameters
- location (`μ` mean parameter)
- scale (`σ^2` variance parameter)

support : `(-∞,∞)` real numbers

as the 'shape' parameter increases (for large `k`, or a `k -> ∞`) the gamma distribution converges to the normal distribution

**in relation to gamma** using the central limit theorem, the gamma (or any distribution with finite variance) will converge to the normal distribution

RIDGE regression, is a bayesian regression with a normal prior

<img src="./imgs/approximated_normal_distribution_25.png" height="300px" width="400px">

### t-distribution (Pearson type VII)
one parameters
- degrees of freedom `𝜈`

**in relation to the gamma** the probability density function is given by the gamma function with the degrees of freedom

support : `(-∞,∞)` real numbers

arises from sampling, estimate the mean of a normally distributed population
- sample size is small
- population standard deviation is unknown

<img src="./imgs/t_distribution.png" height="300px" width="400px">

### fisher's z-distribution
two parameters
- degrees of freedom (`d>0`)
- degrees of freedom (`d>0`)

support : `(-∞,∞)`

for more stats testing

**in relation to gamma** half the log of an f-distribution

<img src="./imgs/fishers_z_distribution.png" height="300px" width="400px">

### generalized normal distribution
three parameters
- location (`μ`)
- scale (`𝛼>0`)
- shape (`β>0`)

support : `(-∞,∞)`

also called the exponential power distribution ot generalized error distribution

**in relation to gamma** built with the gamma function

when `β=2` its the normal distribution, and when `β=1` its the laplce distribution

<img src="./imgs/generalized_normal_distribution.png" height="300px" width="400px">


### cauchy distribution (Pearson type IV)
two parameters
- location (`x` where `x` is real)
- scale (`γ` where `γ > 0`)

support : `(-∞,∞)` real numbers

**in relation to gamma** two independent standard normal divided by one another

cauchy distribution has no mean, variance, or higher moments defined.
The mode and median are defined and equal to the location parameter.

it's the fourier transform of the laplace distribution

`cauchy(0,1)` is a student's t with 1 degree of freedom `t(df=1)`, this is also called the standard cauchy distribution

<img src="./imgs/cauchy_distribution.png" height="300px" width="400px">

### dirichlet distribution
two parameters
- categories (`k`, where `k` is a integer ≥ 2)
- concentration (`𝛼`, where `𝛼 > 0`)

domain ~ thought of as a set of probability distrubtions

**in relation to gamma** the gamma distribution can generate random vectors that form a dirichlet distribution
- `k` independently distributed gamma distributions, each divided by `V` (the sum of the `k` distributions)


multivariate generalization of beta distribution
can be thought of as 'a distribution over distributions'
  - sampling from a dirichlet results in a distribution

symmetric dirichlet distributions - where all parameters are equal.

concentration parameter ~ how concentrated the proabability mass of from the distribution is likely to be
  - with value less than 1 the mass is concentrated in a few components.
  - value greater than 1 the mass is dispersed ~ equal in components.
  
  
  ### logit-normal distribution
two parameters
- squared scale (`σ^2`)
- location (`μ`)

support : `(0,1)`, thanks logistic function

**in relation to gamma** logistic transform of the normal distribution

alternative to the dirichlet distribution, aka it captures correlations in components of probability vectors

<img src="./imgs/logit_normal_distribution.png" height="300px" width="400px">

### pareto distribution
two parameters
- scale (`x`, positive real number > 0)
- shape (`𝛼`, positive real number  > 0)

power-law probability distribution.

used all over the place 80% of the time

**in relation to gamma** the log of a pareto distribution divided by the minimum `x sub m` is an exponential distribution (a specific parameterization of the gamma)

check out relationship to gumbel

<img src="./imgs/pareto_distribution.png" height="300px" width="400px">

### lomax distribution (pareto type II)
two parameters
- shape (`𝛼>0`)
- scale (`λ>0`)

support :`x>=0`

used in queuing theory and internet traffic modeling

**in relation to gamma** lomax distribution is a mixture of exponential distributions, with the rate being a gamma distribution.

a lomax(1,1) distribution is the same as an f(2,2) distribution.

lomax with scale=1 is a special case of the beta prime distribution.

<img src="./imgs/lomax_distribution.png" height="300px" width="400px">

### burr distribution
two parameters
- c (`c>0`)
- k (`k>0`)

support : `x>0`

**in relation to gamma** burr(1, k) is the lomax distribution

<img src="./imgs/burr_distribution.png" height="300px" width="400px">

### rayleigh distribution
one paramter
- scale (`σ`, positive real number > 0)

support : `[0,∞)`

think of magnitude of uncorrelated, normally distributed components.
 
**in relation to gamma** the sum of squared rayleigh distributions is a gamma distribution with`Γ( N, 2 * σ^2 )`. 

the rayleigh distribution of `σ=1` is a chi distribution with `ν=2`, also the square of a rayleigh distribution is a chi-squared distribution with degrees of freedom `k=2`. 

finally the square root of an exponential distribution is a rayleigh distribution with `R(1/ (2λ)^1/2)`


<img src="./imgs/rayleigh_distribution.png" height="300px" width="400px">

### rice distribution
two parameters
- distance from reference point and the center of the bivariate distribution (`ν>=0`)
- spread (`σ>=0`)

support : `[0,∞)`

it the magnitude of a circularly-symmetric bivariate normal random variable

**in relation to gamma** the square of the rice distribution when `ν>=0` is an exponential distribution (which is a case of the gamma distribution).

rice(0,σ) is a rayleigh(σ)

rice distribution is the multivariate generalization of the folded normal distribution

### gumbel distribution (extreme value distribution type I)
two parameters
- location (`μ` real number)
- scale (`β` real number > 0)

support : `(-∞,∞)` x is a real number

**in relation to gamma** its the negative log of an exponential distribution with mean=1, aka the exponential of an exponential.

it models the distribution of the maximum of a number of samples of various distrubtions (pretty meta)

its a generalization of the extreme value distribution

the difference between two gumbel distribution random variables is a logistic distribution

<img src="./imgs/gumbel_distribution.png" height="300px" width="400px">

### fréchet distribution (extreme value distribution type II)
three parameters (two are optional)
- shape (`𝛼` positive real number > 0, the shape is generalized to include the location and scale)
- scale (`s=1` positive real number > 0, default value is 1, so is optional to change)
- location of minimum (`m=0` real number, default value is 0, so it optional to change)

support : `x > m`, for a random variable greater than the minimum

**in relation to gamma** its the negative log of a uniform distribution raised to the negative `1/𝛼`

if the location of the minimum is 0, then the reciprocal is a weibull distribution

<img src="./imgs/frechet_distribution.png" height="300px" width="400px">

### weibull distribution (reversed weibull is extreme value distribution type III)
two parameters
- shape (`λ` real number > 0)
- scale (`k` real number > 0)

support : `[0,∞)`

**in relation to gamma** it is an exponential distribution divided by the shape, raised to the scale parameter.

the weibull distribution is also the negative natural log of the uniform distribution raised to 1 divided by the scale, all multiplied by the shape

when `k=2` the weibull distribution is a rayleigh distribution with `σ=λ/√2`

weibull distribution is the maximum entropy distribution 

the weibull distribution can be thought of as the failure rate proportional to a power of time `k`
- `k<1` the failure rate decreases over time
- `k=1` constant failure rate
- `k>1`failure rate increases over time

there is also a three parameter weibull distribution, with a location parameter `θ` that is the time before the failure (weibull) process begins

<img src="./imgs/weibull_distribution.png" height="300px" width="400px">


### exponential-logarithmic distribution
two parameters
- p (from `(0,1)`)
- beta (`β>0`)

support : `[0,∞)`

**in relation to gamma** the exponential-logarithmic distribution reduces to the exponential distribution when `p goes to 1`.

<img src="./imgs/exponential_logarithmic_distribution.png" height="300px" width="400px">

### gompertz distribution
two parameters
- shape (`eta>0`)
- scale (`b>0`)

support : `[0,∞)`

**in relation to gamma** the gamma distribution is a conjugate prior to gompertz likelihood

<img src="./imgs/gompertz_distribution.png" height="300px" width="400px">

### inverse gamma distribution
two parameters
- shape (`𝛼>0`)
- scale (`β>0`)

support : `(0,∞)`

**in relation to gamma** just invert it (but be careful with scale parameter)

levy distribution is a specific parameterization of the inverse gamma distribution

<img src="./imgs/inverse_gamma_distribution.png" height="300px" width="400px">

### inverse chi-squared
one parameter
- degrees of freedom (`ν`)

support : `(0,∞)`

**in relation to gamma** invert it to get chi-squared (which is a special case of the gamma distribution)

prior and posterior distribution for unknown variance of the normal distribution in bayesian inference

<img src="./imgs/inverse_chi_squared_distribution.png" height="300px" width="400px">

### lévy distribution
two parameter
- location (`μ`)
- scale (`c>0`)

support : `[μ,∞)`

**in relation to gamma** the levy distribution with the `location=0` is an inverse gamma distribution with `shape=1/2`

the inverse of normal distribution minus location parameter is the levy distribution

<img src="./imgs/levy_distribution.png" height="300px" width="400px">

### log-cauchy distribution
two parameters
- location (`μ`)
- scale (`σ`)

support : `(0,∞)`

**in relation to gamma** e raised to the cauchy distribution is the log-cauchy distribution

<img src="./imgs/log_cauchy_distribution.png" height="300px" width="400px">

### log-logistic distribution
two parameters
- scale (`𝛼>0`)
- shape (`β>0`)

support : `[0,∞)`

**in relation to gamma** log-logistic is a specific case of the beta prime distribution

when the shape=1 if log-logistic, it is a generalized pareto distribution

<img src="./imgs/log_logistic_distribution.png" height="300px" width="400px">

### log-normal distribution
two parameters
- location (`μ`)
- scale (`σ`)

support : `(0,∞)`

**in relation to gamma** ^ μ + σ* standard normal distribution

<img src="./imgs/log_normal_distribution.png" height="300px" width="400px">

### maxwell-boltzmann distribution
one parameter
- scale (`a>0`)

support : `(0,∞)`

the scale parameter is speed proportional to the ratio of temperature to particle mass.

**in relation to gamma** is a chi-squared(3) with a scale parameter, the 3 degrees of freedom are the components of the velocity vector


<img src="./imgs/maxwell_boltzmann_distribution.png" height="300px" width="400px">


### continuous bernoulli distribution
one parameter
- shape `λ from (0,1)`

support : `[0,1]`

**in relation to gamma** an exponential distribution from `[0,1]` is equal to a continuous bernoulli distribution, with the corresponding lambda

<img src="./imgs/continuous_bernoulli_distribution.png" height="300px" width="400px">

## Discrete Distributions
starting with the negative binomial distribution, due to relationship with gamma


### negative binomial
two parameters
 - number of failures ('r' where `r > 0`)
 - probability of success (`p`, for each experiment)

number of successes in a sequence of independent and identically distributed (iid) **Bernoulli** trials before `r` failures

can view the negative binomial as **poisson** distribution with `λ` being a random variable with a gamma distribution with shape `r` and scale `θ = p/(1-p)`

under certain parameters the negative binomial converges to the poisson

### mulitnomial distribution
two parameters
- number of trial (`n>0` positive integer)
- event probabilities (`p1, p2, ...` the probabilities sum to 1)

support : 

it's a generalization of the binonmial distribution

### zeta distribution
parameters
- rate? (`s`, where `s`> 1)

which is made from the riemann zeta function

support : positive integers


### yule-simon distribution
one parameter
- shape (`p>0`)

support : positive integers

## To add

### pearson distributions
four (or more) continuous distributions

type I ~ generalized beta distribtuion

type II ~ symmetric type I distributions

type III ~ generalized gamma distribution ~ chi-squared

type IV ~ cauchy distribution

type V ~ inverse gamma distribution

type VI ~ f-distribution or a beta prime

type VII ~ t-distribution


getting normal ~ take the limit of a I, III, IV, V, or VI distribution.


### irwin-hall distribution
one parameter
- number of uniform distribution (`n` natural number)

support : `[0,n]`

uniform sum distribution

**in relation to gamma**
sum of uniform(0,1) distributions



### noncentral chi-squared distribution
two paramters
- degrees of freedom (`k>0`)
- non-centrality parameter (`λ>0`)

support : `[0,∞)`

in case of likelihood-ratio tests

pdf uses the bessel function

**in relation to gamma** linear combo of noncentral chi-squared distributions make a generalized chi-squared distribution

square root of a noncentral chi-squared distribution is a rice distribution


### noncentral t-distribution
two parameters
- degrees of freedom (`v>0`)
- noncentrality (`μ`)

even more stats tests

**in relation to gamma** the probability density function is given by the gamma function with the degrees of freedom, noncentrally of course.

### slash distribution
no parameters!

support : `(-∞,∞)`

just a standard normal distribution divided by a standard uniform distribution

used in simulation, and has heavier tails than a normal distribution

### stable distribution
 four parameters
 - stability (`𝛼` from `(0,2]`)
 - skewness (`β` from `[-1,1]`)
 - scale (`c` from `(0,∞)`)
 - location (`μ`)

a stable distribution is one that is made from a linear combination of tow independent random variables with the same distribution.

support : depends on 𝛼 and β

 special cases
 - cauchy
 - levy
 - normal

 those three have closed form expressions for the PDFs, the rest don't.

### q-exponential distribution
two parameters
- shape (`q<2`)
- rate (`λ>0`)

support : `[0,∞)` for `q>=1`

this is a tsallis distribution

**in relation to gamma** q-exponential distribution is a generalized lomax distribution

q-exponential distribution is a special case of the generalized pareto distribution

### q-gaussian distribution
two parameters
- shape (`q<3`)
- `β>0`

this is a tsallis distribution

support : `(-∞,∞)` for `1<=q<3`

**in relation to gamma** it's a scaled t distribution

### q-weibull distribution
three parameters
- shape (`q<2`)
- rate (`λ>0`)
- shape (`funny k>0`)

support : `[0,∞)` for `q>=1`

this is a tsallis distribution

**in relation to gamma** generalization of weibull and lomax distribution

### phase-type distribution

convolution of exponential distributions

### wishart distribution
matrix_value distribution

gamma distribution generalization to multiple dimensions

### wilks lambda distribution
matrix_value distribution
two independent wishart distributions

for multivariate hypothesis testing

### holtsmark distribution
two parameters
 - scale (`c` from `(0,∞)`)
 - location (`μ`)

support : real numbers

special case of a stable distribution(beta=0, and alpha=3/2), where PDF can be made with the hypergeometric function

### von mises distribution

### tweedie distribution

### tukey lambda distribution

### poisson

### geometric

### log series discrete distribution


## support section

distribution | support | support for vis | ideally
------------ | ------- | --------------- | -------
gamma        | [0,∞)   | (0,20]          | (0,20)
erlang       | [0,∞)   | (0,20]          | (0,20)
exponential  | [0,∞)   | (0,20]          | (0,20)
chi-squared  | [0,∞)   | (0,20]          | (0,20) 
laplace      | real numbers | (0,20)     | (-10,10)
beta         | [0,1]   | (0,1)           | (0,1)
beta prime   | [0,∞)   | (0,5)           | (0,5)
arcsine      | [0,1]   | (0,1)           | (0,1)
uniform      | [0,1]   | (0,1)           | (0,1)
f            | [0,∞)   | (0,5)           | (0,5)
normal       | real numbers | (0,5)      | (-5,-5)
t            | real numbers | (0,5)      | (-5,-5)
cauchy       | real numbers | (0,5)      | (-4,4)
dirichlet    |
pareto       | [x_min,∞) | (0,5)         | (0,5)
rayleigh     | [0,∞)   | (0,5)           | (0,10)
gumbel       | real numbers | (0, 20)    | (-5,20)
fréchet      |  x > m  | (0,5)           | (0,5)
weibull      | [0,∞)   | (0,5)           | (0,2.5)
lévy         | [μ,∞)   | (0,5)           | (0,5)
rice         | [0,∞)   | (0,20)          | (0,20)
kumaraswamy  | [0,1]   | (0,1)           | (0,1)
z            | real numbers | (0,5)      | (-5,-5)
generalized normal distribution |  real numbers | (0,5)      | (-5,-5)
chi          | [0,∞)   | (0,5)           | (0,5)
nakagami     | [0,∞)   | (0,5)           | (0,5)
maxwell-boltzmann | [0,∞)   | (0,20]          | (0,20) 
inverse chi-squared | [0,∞)   | (0,1)           | (0,1)
inverse gamma | [0,∞)   | (0,1)           | (0,1)

## Sources

[wiki list of distributions](https://en.wikipedia.org/wiki/List_of_probability_distributions)
