# KL-Divergence(KL 발산)

어떤 데이터의 확률밀도함수 $p(x)$가 있다고 하자. 이 함수를 정확하게 알 수 없어서 이를 근사적으로 추정한 확률밀도함수 $q(x)$를 사용한다고 가정하자.  이때 실제 확률밀도함수 $p(x)$로 얻을 수 있는 정보량과 추정된 확률밀도함수 $q(x)$로 얻을 수 있는 정보량은 차이가 난다. 이때 이 둘 사이의 평균 정보량이 얼마나 차이가 나는지 계산한 것을 상대 엔트로피(relative entropy) 또는 KL 발산(Kullback-Leibler Divergence)라고 하며 다음과 같이 정의한다.


$$
\begin{align}
D_{KL}(p(x)\parallel q(x)) &= -\int_x{p(x)\log{q(x)}}dx - \left(-\int_x{p(x)\log{p(x)}}dx\right)\\
&= \int_x{p(x)\log{\frac{p(x)}{q(x)}}}dx \\
\end{align}
$$
식 (1)의 우변에서 첫번재 항 $-\int_x{p(x)\log{q(x)}}dx$는 근사 분포인 $q(x)$의 정보량을 실제 분포를 사용해 기대값을 계산한 것이고, 두번째 항 $-\int_x{p(x)\log{p(x)}}dx$은 실제 분포 $p(x)$의 평균 정보량이다. KL 발산은 두 확률분포의 엔트로피 차이를 나타내지만, 두 확률분포가 얼마나 유사한지 '거리'를 측정하는 도구로 쓰인다. 실제로 KL 발산은 거리의 척도(matrix) 특성 4가지 중 3가지만을 만족하고 대칭성을 만족하기 때문에 준(semi) 거리 척도라고 한다.

KL 발산의 정의에 의하면 몇 가지 특징을 추출할 수 있다. 우선 KL 발산은 비대칭 함수다. 즉, 
$$
D_{KL}\left(p(x) \parallel q(x)\right) \ne D_{KL}\left(q(x) \parallel p(x)\right)
$$
이다. 또한 항상 $D_{KL}(p(x) \parallel q(x))\ge 0$을 만족하며, $p(x) = q(x)$일 때만 $D_{KL}(p(x) \parallel q(x)) = 0$을 만족한다. 이는 $-\log()$함수가 convex function임을 이용하여 증명 할 수 있다. Convex function $f(x)$에 대해서는 다음과 같이 젠센 부등식(Jensen's inequallity)이 성립한다.
$$
E\left[f(g(x))\right] \ge f\left(E\left[g(x)\right]\right)
$$
이제, KL 발산 식에서 $g(x) = \frac{q(x)}{p(x)}$ 를 사용해 $f(g(x)) = -\log{g(x)}$로 놓으면, 
$$
\begin{align}
D_{KL}(p(x)\parallel q(x)) &= \int_x{p(x)\log{\frac{p(x)}{q(x)}}}dx = -\int_x{p(x)\log{\frac{q(x)}{p(x)}}}dx\\
&\ge -\log{E\left[\frac{q(x)}{p(x)}\right]} = -\log{\int_x{p(x)\frac{q(x)}{p(x)}}dx}\\
&= -\log{\int_x{q(x)}dx} = -\log{1} = 0
\end{align}
$$
이 되는 것을 알 수 있다.

$p(x)$와 $q(x)$가 각각 평균이 $\mu_p$, $\mu_q$이고, 공분산이  $P_p$, $P_q$인 n차원 가우시안 분포라면 KL 발산은 다음과 같이 계산된다.
$$
D_{KL}(p(x)\parallel q(x)) = \frac{1}{2}\left(tr(P_q^{-1}P_p) +\left(\mu_q - \mu_p\right)^TP_q^{-1}\left(\mu_q - \mu_p\right) - n + \log{\frac{\det{P_q}}{\det{P_p}}}\right)
$$
실제 데이터 분포가 $p(x)$로 주어지고 이를 $q(x)$로 추정하고자 할 때 해당 데이터 집합에서$p(x)$는 고정이므로(물론 알지는 못하지만) $p(x)$와 유사한 $q(x)$를 계산하는 것을 다음과 같이 생각할 수 있다.
$$
\begin{align}
\arg\min_q{D_{KL}(p(x)\parallel q(x))} &=\arg\min_q{\left(-\int_x{p(x)\log{q(x)}}dx+\int_x{p(x)\log{p(x)}}dx\right)}\\
&=\arg\min_q{\left(-\int_x{p(x)\log{q(x)}}dx\right)}\\
&=\arg\min_q{H(p, q)}
\end{align}
$$
즉, 데이터 집합이 주어졌을 때 미지의 $p(x)$와 유사한 $q(x)$는 교차 엔트로피 $H(p,q)$를 최소로 만드는 확률밀도함수이다.