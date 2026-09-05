**3. Probability and Statistics - beans**

A jar contains 3 red beans, 7 green beans, and 10 black beans. If you choose a bean at random, what is the probability it will be black?

Pick ONE option

* 3 / 7
* 3 / 10
* 3 / 20
* 1 / 2 ✅

**4. Probability and Statistics - Flip**

You flip two fair coins. At least one of them is heads. What's the probability that both are heads?

Pick ONE option

* 1/4 
* 1/3 ✅
* 1/2
* 2/3

**5. Calculus - Circle**❓R=r+R 算不出与选项匹配的答案

The radius of a circle is increasing at a nonzero rate, and at a certain instant, the rate of increase in the area of the circle is numerically equal to the rate of increase in its circumference. At this instant, what is the radius of the circle?

Pick ONE option

* 1/pi
* 2/pi
* 1
* 2

思维复现：
设r是t时刻的圆半径，t时刻时恰好面积的increase rate和周长的increase rate 相等，所以设t时刻之前的半径是R, 那我们有(pir^2-piR^2/piR^2)=(2pir-2piR)/2piR呀，如果把rate理解成金融那个比昨天增长百分之多少，然后想办法把R消掉就有了R=r+R

错因：
calculus里面的rate指的就是变量相对与时间t的变化，上面说的概念是“相对增长率”

正确思路：
设r为t时刻的半径，增长速率为，dr/dt
求面积变化率和周长变化率相等的时刻：dpir^2/dt=d2pir/dt
利用链式法则：因为pir^2和2pir表达式里面没有t，不能直接求导，所以 
dpir^2/dt=(dpir^2/dr)\*(dr/dt)=2pir\*dr/dt
d2pir/dt=(d2pir/dr)\*dr/dt=2pi\*dr/dt
2pir\*dr/dt=2pi\*dr/dt , dr/dt！=0，两侧消2pi\*dr/dt得
r=1

**6. Calculus - Cosine Limit**❓忘记怎么求极限了

What is the limit of (Cos(x)-1)/x^2 as x approaches 0?

Pick ONE option

* 1/2
* -1/2
* 1
* -1
* 0
补充知识：
求极限的方式
1.洛必达法则，分0/0型和 ∞/∞型（即将极限位置的代入是否=0或∞）, 对分子分母同时求导，极限不变
2.等价无穷小（求x->0)常见替换口诀：
(1) （反）三角变x: sin(x) / tan(x) / arcsin(x) / arctan(x)
(2) 指对变x: e^x - 1 / ln(1+x)
(3) 唯一要记：$1 - \cos(x)$ ～ （1/2）x^2

正确思路：
1.洛必达法：
lim(x->0)(Cos(x)-1)/x^2=lim(x->0)（-sinx)/(2x)=lim(x->0)(-cosx)/2=-1/2
2.等价无穷小替换法：
lim(x->0)(Cos(x)-1)/x^2=lim(x->0)(-（1/2）x^2)/x^2=-1/2

**7. Linear Algebra: Linear Map**❓不记得怎么算

Let T : R^2 -> R^3 be a linear map satisfying T(2,7) = (1,-2,2) and T(1,2) = (1,-2,1). Calculate the dot product of T(0,3) and (1,1,1).

Pick ONE option

* 0
* 1
* 2
* 3

补充知识：
线性变换的线性性质（Linearity）
1.T(u + v) = T(u) + T(v)
2.T(c \cdot u) = c \cdot T(u)

正确思路：
只要知道两个基向量的变换结果，就可以算出定义域内任意向量的变换结果
1.把目标向量 (0, 3) 表示为已知（基）向量 (2, 7) 和 (1, 2) 的线性组合
设(0, 3)=a(2, 7)+b(1, 2) 解方程得a=1,b=-2
2.利用线性性质(1)求 T(0, 3)
T(0, 3)=T(1(2, 7))+T(-2(1, 2)) 利用性质（2）
T(1(2, 7))=1T(2, 7)
T(-2(1, 2))=-2T(1, 2)
T(0, 3)=1T(2, 7)+-2T(1, 2)=1(1,-2,2)+-2(1,-2,1)=(1,-2,2)+(-2,4,-2)=(-1,2,0)
(-1,2,0)*(1,1,1)=-1+2+0=1

**8. Probability and Statistics - 3 coin flip game** ❓看不懂题目

We have a game, where we each flip 3 coins. If we have the same number of heads, then you get 2^n where n is the number of heads. What is the expected value of this game?

Pick ONE option

* 31/32
* 23/32
* 1
* 63/64

思维复现：
“you"和“we"是什么关系，2^n又是什么

解释：
"we" 指的是两个人（即“你”和“我”），这是一个双人游戏，2^n是奖金数目，只有当两人heads数相等时，才得2^n数量的奖金，expected value of this game求的是"you"得到的奖金,n是一个人的head数

正确思路：
P(两人同时有0个head):C(3,0)(1/2)^3 x C(3,0)(1/2)^3=1/64
P(两人同时有1个head):C(3,1)(1/2)(1/2)^2 x C(3,1)(1/2)(1/2)^2=9/64
P(两人同时有2个head):C(3,2)(1/2)^2(1/2) x C(3,2)(1/2)^2(1/2)=9/64
P(两人同时有3个head):C(3,3)(1/2)^3 x C(3,3)(1/2)^3=1/64

期望=1/64x2^0+9/64x2^1+9/64x2^2+1/64x2^3=1/64+18/64+36/64+8/64=63/64

**9. Calculus - Taylor Expansion** ❓不记得怎么求一个式子的泰勒展开

If f(x) = 1/x, what is the leading coefficient of the 12th Taylor polynomial centered at 1?

Hint: This is the coefficient in front of (x-1)^12.

Pick ONE option

* 1
* -1
* 1/12
* -1/12

补充知识：
1.f(x) 在 x=a处的泰勒级数展开：sum(n=0,(f^n(a)/n!)(x-a)^n)

思路：
f^n(a)/n!a=1, n=12, f^12(1)=12!,结果为1

**10. Linear Algebra - Sub spaces**

Which of the following vectors does NOT belong to the subspace spanned by -2i + 3j + k and i + j + 2k?❓不记得怎么算

Pick ONE option

* -4i + 6j + 2k
* 3i + 8j + 11k
* 11i - 4j + 6k
* 10i - 5j + 5k

思路（直接观察+二算一验）：
-2i + 3j + k对应的基向量v1=(-2,3,1);i + j + 2k对应的基向量v2=(1,1,2)
A （-4，6，2）直接观察=2v1，在
B 配不出来解方程，-2a+b=3,3a+b=8,解出a=1,b=5, 代入a+2b=11验证,在
C -2a+b=11,3a+b=-4,a=-3,b=5, 代入a+2b=6验证,不在
D -2a+b=10,3a+b=-5,a=-3,b=4, 代入a+2b=5验证,在
选C

**3. Probability and Statistics - Movies** ❓没思路

There are 5 movie CDs. Two people A and B have a preference order among the 5 movies that the other person does not know. The distribution of preference order is uniform for both the persons and is independent among the two. They both do the following. A removes two of his least preferred movies out of the five movies. B then removes two of his least preferred movies from the remaining three movies. The movie which remains at the end is the one that they watch. What is the probability of neither of them getting to watch their favorite movie?

Pick ONE option:

* 4/15
* 2/15
* 3/8
* None of the Above

思路：
设每部电影为M1,M2,M3,M4,M5
删电影逻辑转化为：A保留自己最喜欢的3部，然后B再从这3部中保留最喜欢的1部
最终看的这部记为Mwatched

两人都没看成最爱的条件：
设两人最喜欢的电影分别为Afav,Bfav, Mwatched!=Afav and Mwatched!=Bfav
即Afav被B淘汰掉了，A留下的3部里，有B认为排名高于Afav的电影
Bfav排在A认为的最后两名里

case1: Afav=Bfav(概率为1/5)
因为Afav一定会进入前3名，所以此case不存在
case2:Afav!=Bfav (概率为4/5)
（1）Bfav落入A的后2名的概率是：2/4=1/2，因为已知Afav!=Bfav
在（1）的条件下，Afav被B淘汰(即B不选A选择留下另外两部其中一部)的概率是：2/3

4/5*1/2 * 2/3=4/15


**11. Calculus - Hard Continuity with Rationals Denominators** ❓没思路

Function mapping:

F maps (0,1) -> [0,1].

Function definition:

F(x) = 0 if x is irrational, and F(x) = 1/q if x is rational with reduced form p/q, where p and q are relatively prime integers.

Question:

Which of the following is correct?

Options:

* F is continuous on its full domain
* F is nowhere continuous
* F is continuous on the irrationals but not on the rationals
* F is continuous on the rationals but not on the irrationals

补充知识：
连续的定义：lim(x->a)F(x)=F(a)极限值等于函数值

思路：
1.看有理数位置是否连续：1/2是有理数，F(1/2)=1/2 (p=1,q=2), 1/2附近有无数个无理数，函数值为0，1/2处极限为0,极限值不等于函数值，不连续，排除A,D
2.看无理数位置是否连续：
case1: 从无理数靠近无理数点，连续
case2:从有理数靠近无理数点，即用有理数逼近无理数，q->∞，所以极限值趋于0，连续
选C

**4. Probability and Statistics - interpreting CIs** ❓概念不清

**Premise:**

Suppose a coin is tossed 80 times, yielding a calculated sample mean of 0.56, a 90% confidence interval of [0.61, 0.52], and a 99% confidence interval of [0.63, 0.49]. What conclusion can be drawn?

**Options:**

* the coin is fair with certainty p < 0.01
* the coin is not fair with certainty p < 0.01
* the coin is not fair with certainty p < 0.1, but not p < 0.01
* the coin is fair with certainty p < 0.1, but not p < 0.01

补充知识：
1. 置信区间(Confidence Interval)
2. 假设检验(Hypothesis Testing)
3. p-value
https://www.bilibili.com/video/BV1yf4y1K7so/?spm_id_from=333.337.search-card.all.click&vd_source=9902916331bef4c93586d2ad5780e0b0
思路：
1.零假设 H0:p=0.5(假设硬币公平),被择假设H1:P!=0.5(硬币不公平)
2.现在去硬币里抽样，总体是这80次实验，抽样结果为miu=0.56,p<0.1的情况抽到 x>0.61或者x<0.52,p=0.5不在这个区间内，所以要在p value <0.1的显著性下推翻H0选择H1
3.p=0.5在[0.63, 0.49]区间内，所以没有足够证据在p value <0.01的显著性下推翻H0
选C


**6. Calculus - Bounding an Integral**

If Iₙ = ∫ xⁿ (1+x)^0.5 dx , n = 0,1,2...

where the integral is for x ∈ [0,1].

By first finding a bound on the integrand, which of these is an upper bound on Iₙ?

Pick ONE option

- 1/(n+1) ✅
- 1/2(n+1)
- 1/(n+1) + 1/(n+2)
- n^n

补充知识：
1.求函数反导

正确答案应该选1/(n+1) + 1/(n+2)


**7. Linear Algebra - Eigenvalues 2** ❓概念不清

Eigenvectors of matrix A = [ 1 2; 2 3]

Pick ONE option

- are not distinct
- are imaginary
- can be chosen to be orthogonal
- can be uniquely specified

补充知识：
1.谱定理（Spectral Theorem）任何实对称矩阵的特征值必定全是实数，且对应的特征向量可以选为相互正交的。
2.只要矩阵不对称，特征值就有可能解出复数
3.特征向量与特征值：对于一个方阵 A，如果存在一个非零向量 x 和一个标量 lambda，
    满足：Ax = lambda x，lambda就是特征值，x是特征向量
4.求解特征值：det(A-lambda I)=0 (A-lambda I)不可逆
5.行列式（Determinant）的几何意义：代表矩阵变换后的空间体积缩放比例。
6.n>2行列式求解：高斯消元法，上三角/下三角矩阵行列式，等于其主对角线元素的乘积
7.求解特征向量：将特征值代入(A-lambda I)x=0，令x1等于任何非零实数，算出x2。

思路：
1.由谱定理可知，A为实对称矩阵，特征值为实数，所以特征向量也是实数，排除B
2.特征向量绝对不可能有唯一解，排除D
3.结果求出特征值是两个互不相同的值，所以特征向量是两个互不相同的,排除A
4.算内积=0，正交选C

**9. Calculus - Maximize Expected Value** ❓我知道是求导，但是（1+e^x)^-1的导数如何=0？

A seller is trying to sell an antique. As the seller's offer price x increases, the probability p(x) that a client is willing to buy at that price decreases with the function p(x) = 1 / ( 1 + eˣ). The seller aims to set an offer price, x₀ to maximize the expected value from selling the antique. Which of the following is true about x₀?

Pick ONE option

- eˣ⁰(x₀ − 1) − 1 = 0
- eˣ⁰(1 − x₀) = e
- To maximize the expected value, x₀ should be set as high as the auction allows.
- None of the above.

错因：要对期望收益求导，而不是概率函数本身求导

补充知识：
分数求导：分母的平方分之，子导母不导-子不导母导

思路：
期望收益函数为，p(x)乘以商品价值x,即 xp(x),求导结果为1+eˣ-xeˣ=0,左右乘-1答案为A

**10. Linear Algebra - Linear Equation Statements** ❓有点不记得了

Consider a linear equation system Ax = b, where A is r x n. How many statements below are true?

1. If r ≤ n, then it must have at least one solution.✅
2. If r > n, then it must have no solution.
3. If b = 0, then it must have a solution.✅
4. If r = n, then it has a unique solution if and only if det(A) ≠0.

Pick ONE option

- 0
- 1
- 2
- 3

思路：
r<=n意味着方程数小于或等于未知数，通常有无穷多解，但是也有inconsistent导情况下是无解的
r>n意味着方程数大于未知数，如果consistent也是有可能有解的
b=0肯定有一平凡解
r=n det(A) ≠0 iff方阵可逆，方针可逆Ax=b等式两边乘A-1,x=A-1b,是唯一解

**11. Probability & Statistics - Bernoulli Variables** ❓不知道怎么求和，分母是什么

Let X₁, X₂, …, X₁₀₀ all be independent Bernoulli variables, which take a value of 1 with probability 0.5. Estimate the probability that X₁ + X₂ + … + X₁₀₀ < 60.

Pick ONE option

- 0.5000
- 0.8400
- 0.9750
- 0.9985

补充知识：
1.中心极限定理：在许多情况下，对于独立并同样分布的随机变量，即使原始变量本身不是正态分布，标准化样本均值的抽样分布也趋向于标准正态分布。(n>=30)
2.期望和方差的线性累加性质，
    E[X1+X2+...+Xn]=E[X1]+E[X2]+...+E[Xn]
    Var(X1+X2+...+Xn)=Var(X1)+...+Var(Xn)
3.伯努利分布方差公式：p(1-p)
4.标准化(z-score)转换:(S-miu/sigma)用于标准正态分布查表
5.3sigma原则概率：P(Z<1)0.84，P(Z<2)0.9750，P(Z<3)0.9985

思路：这里n=100是算大样本的，可以近似（Estimate）为正态分布求解
这个近似的正态分布的E为100*0.5=50，方差为100\*0.5\*(1-0.5)=25，标准差为5
(S-miu/sigma)=(S-50/5)=2
P(S<60)=P(Z<2)选C

**8. Probability & Statistics - Disease Probability**

Suppose you go in for testing for a disease that one in every 100 people have. If you have the disease, there is a 50% probability you will test positive. If you don't have the disease, there is still a 50% probability you will test positive. Given that your test is positive, what is the probability you have the disease?

Pick ONE option

- .5
- .005✅
- .01
- .05


用贝叶斯定理，答案选C

6. Calculus - Sequences ❓不记得怎么算

What is the limit of the sequence aₙ = 6/(1+aₙ₋₁) if a₀ = 1?

Pick ONE option

补充：
1.递推式算极限：假设极限存在，用不动点解候选极限L
2.数列求极限，默认是求n->∞

思路：
如果极限L存在，aₙ 和 aₙ₋₁ 都趋近于L,两边同时取极限：L=6/(1+L) 解方程得L=2或L=-3
排除不合理的根，因为aₙ恒正，索引L=2
也可以多试几个值，观察规律

8. Probability and Statistics - Balls and Bins 

Starting with n empty bins and an infinite supply of balls, each ball is thrown sequentially to one of the bins selected independently and randomly. The process continues while at least one bin is empty and stops as soon as all bins have at least one ball. What is the expected number of total balls used in the process (for large n)? ❓不会做

补充知识：
1.几何分布（Geometric Distribution）：关注“尝试多少次才能等到第一次成功”，假设第k次成功，那么前面k-1次全部失败，概率为p^k-1 *p^k, 期望为1/p
2.渐进式

思路:
假设已经有 k 个桶里装了球，现在要扔球，直到有一个球落入剩下的 n - k 个空桶中
设成功概率（当次球落入空桶的概率）为pk,pk=（n-k）/n
期望E[pk]为n/(n-k),各阶段累加就是n(1/n+1/(n-1)+...+1/1 )
调和级数渐进是ln n, 所以答案是nln n

9. Calculus - Length of a Curve

Find the length of the piece of curve described by y=(1/2)x^2 +1 for x in [0,1]. 1 不确定是不是导数的定积分

补充知识：弧长公式sqrt(1+(dy/dx)^2) dx

思路：
对弧长公式求定积分，dy/dx=x
L=integral(b,a) sqrt(1+(dy/dx)^2) dx

**10. Linear Algebra - Square Matrices**

Suppose A and B are n-th order square matrix, x = (x₁,x₂,x₃, ..., xₙ)T, and XᵀAX = XᵀBX. Then A = B holds when which of the following holds?

Pick ONE option ❓不会

- r(A) = r(B)
- Bᵀ=B
- Aᵀ=A
- Bᵀ=B and Aᵀ=A

思路：

5. Calculus - Limits

Compute lim(h->0) integral(1,1+h)(root(x5 + 8))dx/h 不会算

**4. Probability**
Two people arrive at a room at random times between 3:00 and 4:00, each staying for 10 minutes. What is the probability that the two people meet in the room at the same time? 泊松分布？不记得了

**5. Calculus** 分部积分？不记得了
Find the limit as a → +∞ of the integral from 0 to 10 of [sin(at) f(t)] dt.

**6. Linear Algebra** 矩阵的幂怎么算？
If A = [1 0; a 1], what is A^k? ans:[1 0; k*a 1]

**7. Linear Algebra**
x₀ is a least square solution of Ax = b. What is the geometric meaning of r = Ax₀ − b? 什么是least square solution？

**8. Brownian Motion**
Let Xt be a Brownian Motion, with X₀ = 0, X₁ > 0. Find P(X₂ < 0). Brownian Motion是什么

**9. Probability**
Roll three dice. What is the probability that the three dice show values in increasing order? 不知道这题如何可以算得快一点

**10. Calculus**
If 1 + ax² is tangent to y = x at one point, find the value of a. 1/2

**11. Linear Algebra** 什么是least square solution？
A = [1 3; 1 -1; 1 1], B = [5; 1; 0]. Find the least square solution of Ax = B.

**12. Linear Algebra** 忘了大矩阵怎么求det了
A is a 2n × 2n matrix, with n a's on the main diagonal (top-left to bottom-right) and n d's, and n b's and n c's on the anti-diagonal (top-right to bottom-left), with all other entries equal to 0. What is the determinant of this matrix?
