[toc]
# **Part1 Linux基础**
## lesson 19
###  目标
#### 查看目录内容
	ls
#### 切换目录
	cd
#### 创建和删除操作
	touch
	rm
	mkdir
#### 拷贝和移动文件
	cp
	mv
#### 查看文件内容
	cat
	more
	grep
#### 其他
	echo
	重定向 > 和 >>
	 管道｜

## lesson 21
	查看隐藏文件和返回上一级
### ls命令说明
以 . 开头的文件为隐藏文件，需要 -a 选项才能看到

. 表示当前目录

.. 表示上级目录

## lesson 22

-l 制表方式显示文件详细信息

-h 配合 -l 使用，人性化方式显示文件大小

## lesson 23
### 通配符的使用

| **通配符** |     **含义**      |
| :----| :-------- |
| * |代表任意个数任意字符|
|?|代表任意一个字符，至少1个|

#### *通配符参考链接：*
https://www.cnblogs.com/ysuwangqiang/p/11364173.html

## lesson 24
### 通配符的字符组
| **通配符** |     **含义**      |
| :----| :-------- |
|[] |表示可以匹配字符组中的任意一个|
|?|代表任意一个字符，至少1个|
|[]|表示可以匹配字符组中的任意一个|
|[abc]|匹配abc中的任意一个|
|[a-f]|匹配从a到f范围内的任意一个字符|

## lesson 25
### CD

* cd 英文单词**change directory**的缩写，功能为改变当前工作目录
* cd - 可以在最近两次的工作目录间切换

## lesson 26-相对路径和绝对路径
* 相对路径 最前面不是/ 或者 ～，表示相对** 当前目录 ** 所在的目录位置
* 绝对路径 最前面是/ 或者 ～，表示从 **根目录/家目录** 开始的具体目录位置
## lesson 27-touch和mkdir命令的扩展

### touch
	* 创建文件或修改文件时间
		* 如果文件不存在，创建空白文件
		* 如果文件已经存在，修改文件的末次修改日期
### mkdir
	* 创建一个新的目录
| **选项** |     **含义**      |
| :----| :-------- |
|-p|递归创建目录|

	* 注意：linux中，文件与目录不可以重名

## lesson 28 rm命令扩展

### rm

## lesson 29
## lesson 30

# **Part2 python基础**

## lesson 131-Python简介
### 认识Python

>*人生苦短，我用Python ---- Life is short , you need Python*

<img src="/Users/derek/Library/Application Support/typora-user-images/image-20201019103902279.png" align="left" alt="image-20201019103902279" style="zoom:80%;" />



**目标**
	* python的起源
		解释器为c语言实现，可直接调用c库文件
	* 为什么用python
	* 特点
	* 优缺点

### 01.Python的起源
> *Python 的创始人为吉多•范罗苏姆（Guido van Rossum）*

<img src="/Users/derek/Library/Application Support/typora-user-images/image-20201019104445396.png" align="left" alt="image-20201019104445396" style="zoom:100%;" />

（略）

#### 1.1 解释器（科普）

**计算机不能直接理解任何除机器语言以外的语言，**所以必须把程序员所写的程序语言翻译成机器语言，计算机才能执行程序。**将其他语言翻译成机器语言的工具，被称为编译器**

编译器翻译的方式有两种：一个是**编译**，另外一个是**解释**。两种方式之间的区别在于**翻译时间点的不同。当编译器以解释方式运行的时候，** 也称为**解释器**

![image-20201019104755800](/Users/derek/Library/Application Support/typora-user-images/image-20201019104755800.png)

#### 1.2 Python的设计目标

1999年，吉多.范罗苏姆向DARPA 提交了一条名为"Computer Programming for Everybody"的资金申请，并在后来说明了他对Python的目标：

* 一门**简单直观的语言**并与主要竞争者一样强大
* **开源**，以使任何人都可以为它做贡献
* 代码**像纯英语那样容易理解**
* 适用于**短期**开发的日常任务

这些想法中的基本都已经成为现实，Python已经横位一门流行的编程语言

#### 1.3 Python 的设计哲学

1. 优雅
2. 明确
3. 简单

* Python 开发者的哲学：**用一种方法，最好是只有一种方法来做一件事**
* 如果面临多种选择，Python开发者一般会拒绝花俏的语法，而选择 **明确没有或者很少有歧义的语法**

> ***在python社区，吉多被称为“仁慈的独裁者”***

#### 02. 为什么选择 Python

* 代码量少
* ........

> ***同一个问题，用不同的语言解决，代码量差距还是很多的，一般情况下，`Python`是`Java`的1/5，所以说 人生苦短，我用Python***

#### 03. Python 特点











## lesson 132 第一个程序



## lesson 133 执行Python的方式



## lesson 134 Pycharm的初始设置1



## lesson 135 Pycharm的初始设置2



## lesson 136 程序注释和算数运算



## lesson 137 程序执行原理



## lesson 138 变量使用及类型



## lesson 139 变量的计算和输入输出



## lesson 140 变量的命名



## lesson 141 if判断语句1



## lesson 142 if判断语句2



## lesson 143 石头剪刀布



## lesson 144 循环目标确定



## lesson 145 循环三大流程介绍



## lesson 146 循环语法介绍和应用场景



## lesson 147 第一个while循环



## lesson 148 单步调试while循环



## lesson 149 死循环的概念和解决方法



## lesson 150 赋值运算符



## lesson 151 程序计数从0开始



## lesson 152 循环计算思路分析



## lesson 153 偶数求和—准备偶数



## lesson 154 偶数求和—计算结果
## lesson 155
## lesson 156
## lesson 157
## lesson 158
## lesson 159
## lesson 160
## lesson 161
## lesson 162
## lesson 163
## lesson 164
## lesson 165
## lesson 166
## lesson 167
## lesson 168
## lesson 169
## lesson 170
## lesson 171
## lesson 172
## lesson 173
## lesson 174
## lesson 175
## lesson 176
## lesson 177
## lesson 178
## lesson 179
## lesson 180
## lesson 181
## lesson 182
## lesson 183
## lesson 184
## lesson 185
## lesson 186
## lesson 187
## lesson 188
## lesson 189
## lesson 190
## lesson 191
## lesson 192
## lesson 193
## lesson 194
## lesson 195
## lesson 196
## lesson 197
## lesson 198
## lesson 199
## lesson 200
## lesson 201
## lesson 202
## lesson 203
## lesson 204
## lesson 205
## lesson 206
## lesson 207
## lesson 208
## lesson 209
## lesson 210
## lesson 211
## lesson 212
## lesson 213
## lesson 214
## lesson 215
## lesson 216
## lesson 217
## lesson 218
## lesson 219
## lesson 220
## lesson 221
## lesson 222
## lesson 223
## lesson 224
## lesson 225
## lesson 226
## lesson 227
## lesson 228
## lesson 229
## lesson 230
## lesson 231
## lesson 232
## lesson 233
## lesson 234
## lesson 235
## lesson 236
## lesson 237
## lesson 238
## lesson 239
## lesson 240
## lesson 241
## lesson 242
## lesson 243
## lesson 244
## lesson 245
## lesson 246
## lesson 247
## lesson 248
## lesson 249
## lesson 250
## lesson 251
## lesson 252
## lesson 253
## lesson 254
## lesson 255
## lesson 256
## lesson 257
## lesson 258
## lesson 259
## lesson 260
## lesson 261
## lesson 262
## lesson 263
## lesson 264
## lesson 265
## lesson 266
## lesson 267
## lesson 268
## lesson 269
## lesson 270
## lesson 271
## lesson 272
## lesson 273
## lesson 274
## lesson 275
## lesson 276
## lesson 277
## lesson 278
## lesson 279
## lesson 280
## lesson 281
## lesson 282
## lesson 283
## lesson 284
## lesson 285
## lesson 286
## lesson 287
## lesson 288
## lesson 289
## lesson 290
## lesson 291
## lesson 292
## lesson 293
## lesson 294
## lesson 295


# **Part3 面向对象**



## lesson296 oop基本概念



## lesson297 类和对象的基本概念
### 01.类和对象的概念
#### 1.1 类

* 类 是对一群具有 **相同 特征** 或者 **行为** 的食物的一个统称，是抽象的，**不能直接使用**
  * **特征** 被称为 **属性**
  * **行为** 被称为 **方法**
* 类就相当于制造飞机时的图纸，是一个 ** 模板 **，是 **负责创建对象的 **

#### 1.2 对象

* **对象**是**由类创建出来的一个具体存在**，可以直接使用
* 由 **哪一个类** 创建出来的 **对象**，就拥有在 **哪一个类** 中定义的：
	* 属性
	* 方法
* **对象** 就相当于用 **图纸** **制造** 的飞机
	*在程序开发中，应该**先有类，再有对象***
	
### 02.类和对象的关系

* **类是模板**，**对象** 是根据 **类** 这个模板创建出来的，应该 **先有类，再有对象**

* **类** 只有一个， 而 **对象** 可以有很多个
	
	* **不同的对象** 之间 **属性** 可能会各个不同
	
* **类** 中定义了什么 **属性和方法**，**对象** 中就有什么属性和方法，**不可能多，也不可能少**

## lesson298 类的三要素和名词提炼法

### 03.类的设计
在使用面向对象开发前，应该首先分析需求，确定一下，程序中需要包含哪些类

![image-20201004213021642](/Users/derek/Library/Application Support/typora-user-images/image-20201004213021642.png)

在程序开发中，要审计一个类，通常需要满足一下三个要素：

1. **类名** 这类事物的名字，**满足大驼峰命名法**
2. **属性** 这类事物具有什么样的特征
3. **方法** 这类事物具有什么样的行为



**大驼峰命名法**
	CapWords

1. 每个单词的首字母大写
2. 单词与单词之间没有下划线

#### 3.1 类名的确定
名词提炼法 分析 整个业务流程， 出现的 名词，通常就是找到的类

#### 3.2 属性和方法的确定
* 对 **对象的特征描述**，通常剋定义为 **属性**

* **对象具有的行为**（动词），通常可以定义为 **方法**
	
	*提示：需求中没有涉及的属性或者方法在设计类时，不需要考虑*
	
#### **练习1**
**需求**

* **小明** 今年 **18岁**，**身高****1.75**，每天早上 **跑** 完步，回去 **吃** 东西

* **小美** 今年 **17岁**，**身高1.65**，小美不 **跑** 步，小美喜欢 **吃** 东西

![image-20201005105336997](/Users/derek/Library/Application Support/typora-user-images/image-20201005105336997.png)

#### **练习2**
**需求**

* 一只 **黄颜色** 的狗 叫 **大黄**

* 看见生人 **汪汪叫**

* 看见家人 **摇尾巴**

  ![image-20201005105747180](/Users/derek/Library/Application Support/typora-user-images/image-20201005105747180.png)

## Lesson 299 内置的dir函数
### 目标
* dir 内置函数
* 定义简单的类（只包含方法）
* 方法中的self 参数
* 初始化方法
* 内置方法和属性
### 01. dir内置函数（知道）
	* 在python中 对象几乎是无所不在的，我们之前学习的变量、数据、函数 都是对象
在python中可以使用以下两个方法验证：
1. 在标识符/数据 后输入一个 . ，然后按下 TAB键，iPython会提示该对象能够调用的 方法列表

2. 使用内置函数dir 传入标识符/数据，可以查看对象内的 所有属性及方法

  提示 \__方法名__ 格式的方法是Python提供的内置方法/属性，稍后会给大家介绍一些常用的 内置方法/属性

| **序号** |     **方法名**      |**类型**|**作用**|
| :----| :-------- | -----| -----|
|01|\__new__|方法|创建对象时，会被 **自动** 调用|
|02|\__init__|方法|对象被初始化时，会被 **自动** 调用|
|03|\__del__|方法|对象被从内存中销毁前，会被 **自动** 调用|
|04|\__str__|方法|返回对象的描述信息，print 函数输出使用|

**提示**：利用dir()函数，无需死记硬背

## lesson 300 定义类基本语法
### 02. 定义简单的类（只包含方法）
**面向对象** 是 **更大** 的 **封装**，在 一个类中 **封装多个方法**，这样 通过这个
类创建出来的对象，就可以直接调用这些方法了

#### 2.1 定义只包含方法的类
在python中定义一个只包含方法的类，语法格式如下：

	class 类名:
		def 方法1(self,参数列表):
			pass
		def 方法2(self,参数列表):
			pass

* **方法** 的定义格式和之前学习过的**函数** 几乎一样
* 区别在于第一个参数必须是 self，暂时记住

	注意：**类名** 的命名规则 要符合 ** 大驼峰命名法 **

#### 2.2 创建对象

* 当一个类定义完成之后，要使用这个类来创建对象，语法格式如下：

	`对象变量 = 类名()`
	
## Lesson 301 简单类案例演练

#### 2.3 第一个面向对象程序
需求
* **小猫** 爱 吃鱼，小猫 要 喝水
  分析
  1.定义一个猫类 `Cat`
  2.定义两个方法 `eat` 和 `drink`
  3.按照需求 - - 不需要定义属性

  ![image-20201007093932315](/Users/derek/Library/Application Support/typora-user-images/image-20201007093932315.png)

```python
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


Tom = Cat()
Tom.eat()
Tom.drink()
```
**引用概念的强调**
在面向对象中，**引用**的概念是同样适用的

* 在Python中使用类 **创建对象之后**，tom 变量中 仍然记录的是 **对象在内存中的地址**

* 也就是 tom **变量 引用** 了**新建的猫对象**

* 使用 print输出 对象变量，默认情况下，是能够输出这个变量 引用的对象是由哪一个类创建的对象，以及在内存中的地址（十六进制表示）
	提示：在计算机中，通常使用 十六进制  表示 内存地址

  * 十进制 和 十六进制 都是用来表达数字的，只是表示的方式不一样
  * 十进制 和 十六进制 的数字之间可以来回转换
	
  * %d 可以以 ** 10进制 ** 输出数字

  * %x 可以以 ** 16进制 ** 输出数字

## Lesson 303 创建多个猫对象

**案例进阶 - - 使用Cat类再创建一个对象**

```python
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
```

​	***提问***： *Tom* 和 *lazy_cat* ***是同一个对象么***？

## Lesson 304 在类的外部给对象增加属性


### 03.方法中的self参数

#### 3.1 案例改造 -- 给对象增加属性
* 在 Python 中，要 **给对象设置属性**，非常的容易，**但是不推荐使用**
  
    * 因为：对象属性的封装应该封装在类的内部
* 只需要在 **类的外部代码**中直接通过`.` 设置一个属性即可
	***注意：这种方法虽然简单，但是不推荐使用***
```python
	Tom.name = "Tom"
	...
	lazy_cat.name = "大懒猫"
```

#### 3.2 使用self 在方法内部输出每一只猫的名字

  * 由 ***哪一个对象 *** 调用的方法，方法内的`self` 就是 *** 哪一个对象的引用 ***
* 在类封装的方法内部，`self`就表示 **当前调用方法的对象自己**
* **调用方法时**，不需要传递参数 `self`
* **在方法内部**
  * 可以通过`self.` 访问对象的属性
  * 也可以通过 `self.` **调用其他的对象方法**
* 改造代码如下：

```python
class Cat:
    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
Tom = Cat()
# 利用 .属性名 赋值语句设置变量属性（不推荐）
Tom.name = "tom"

Tom.eat()
Tom.drink()
```

## Lesson 306 初始化方法1
### **04.初始化方法**
#### 4.1 之前代码存在的问题 -- 在类的外部给对象增加属性

* 将案例代码进行调整，**先调用方法 再设置属性，** 观察一下执行效果

```python
  class Cat:
      def eat(self):
          # 哪一个对象调用的方法，self就是哪一个对象的引用
          print("%s爱吃鱼" % self.name)
  
      def drink(self):
          print("小猫要喝水")
  
  
  # 创建猫对象
  Tom = Cat()
  
  Tom.eat()
  Tom.drink()
  
  # 利用 .属性名 赋值语句设置变量属性（不推荐）
  Tom.name = "tom"
```

* 程序执行报错如下：

```python
  AttributeError: 'Cat' object has no attribute 'name'
  属性错误：‘Cat‘ 对象没有 ’name‘ 属性
```

**提示**

* 在日常开发中，不推荐在 **类的外部** 给对象增加属性

  * **如果在运行时，没有找到属性，程序会报错**
* 对象应该包含有哪些属性，应该 **封装在类的内部**

## Lesson 307 初始化方法2
#### 4.2 初始化方法
* 当使用 `类名()` 创建对象时，会 **自动** 执行一下操作
  1. 为对象在内存中 **分配空间** -- 创建对象
  2. 为对象的属性 **设置初始值** -- 初始化方法（init）
* 这个 **初始化方法** 就是 `__init__`方法，`__init__`是对象的**内置方法**
    `__init__` ***方法是专门用来定义一个类 具有哪些属性的方法***
  在Cat中增加`__init__`方法，验证该方法在创建对象时会被自动调用

```python
class Cat:
    """这是一个猫类"""
    def __init__(self):
        print("这是一个初始化方法")


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
```
## Lesson 308 初始化方法3
#### **4.3 在初始化方法内部定义属性**

* 在`__init__` 方法内部使用 `self.属性名 = 属性的初始值` 就可以 **定义属性**

* 定义属性之后，再使用`Cat`类创建的对象，都会拥有该属性

```python
class Cat:
    """这是一个猫类"""

    def __init__(self):
        print("这是一个初始化方法")
        self.name = "tom"

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat()
tom.eat()
```

## Lesson 309 初始化方法4
#### **4.4 改造初始化方法 -- 初始化的同时设置初始值**

* 在开发中，如果希望在 **创建对象的同时，就设置对象的属性，** 可以对`__init__`方法进行 **改造**
  1. 把希望设置的属性值，定义成`__init__`方法的参数
  2. 在方法内部使用`self.属性 = 形参` 接收外部传递的参数
  3. 在创建对象时，使用`类名(属性1,属性2...)` 调用
```python
class Cat:
    """这是一个猫类"""

    def __init__(self, vName):
        print("这是一个初始化方法")
        self.name = vName

    def eat(self):
        print("%s爱吃鱼" % self.name)


# 使用类名()创建对象的时候，会自动调用初始化方法 __init__
tom = Cat("Tom")
tom.eat()
lazy_cat = Cat("大懒猫")
lazy_cat.eat()
```
## Lesson 310 内置方法del
### 05. 内置方法和属性
| **序号** | **方法名** |  **类型** | **作用** |
| :--|:----:|:-------- |:-------- |
|01|`__del__`|方法|**对象被从内存中销毁**前，会被 **自动** 调用|
|02|`__str__`|方法|返回**对象的描述信息**，print 函数输出使用|

#### 5.1 __del__ 方法（知道）
* 在`Python`中

  * 当使用`类名()`创建对象时，为对象 分配完空间后，自动 调用`__init__`方法

  * 当一个 对象被从内存中销毁 前，会 自动 调用`__del__`方法
* 应用场景
  * `__init__`改造初始化方法，可以让创建对象更加灵活
  * `__del__`如果希望在对象销毁前，再做一些事情，可以考虑`__del__`方法
* 生命周期
  * 一个对象从调用`类名()`创建，生命周期开始
  * 一个对象的`__del__`方法一旦被调用，生命周期结束
  * 在对象的生命周期内，可以访问对象属性，或者让对象调用方法

```python
class Cat:
    def __init__(self,vName):
        self.name = vName

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 离开了" % self.name)


tom = Cat("Tom")


tom.eat()

# del关键字可以删除对象，这样删除会在线上执行
# del tom

# 全局变量，会在下面这行代码执行后才销毁
print("-" * 50)
```

## Lesson 311 内置方法str

#### 5.2 \__str__方法

* 在`Python`中，使用`print`输出 **对象变量**，默认情况下，会输出这个变量 **引用的对象**是由哪一个类 **创建的对象**，以及 **内存中的地址（十六进制表示）**

* 如果在开发中，希望使用`print`输出 **对象变量**时，能够打印 **自定义的内容**，就可以利用`__str__`这个内置方法了

 ***注意：`__str__`方法必须返回一个字符串*** 

## Lesson 312 面向对象练习1

### **面向对象封装案例**

**目标**

* 封装
* 小明爱跑步
* 存放家具

### 01. 封装

1. **封装** 是面向对象编程的一大特点
2. 面向对象编程的 **第一步** --  将 **属性** 和 **方法** **封装**到一个抽象的 **类**中
3. 外界 使用 **类** 创建 **对象**，然后 **让对象调用方法**
4. 对象方法的细节 都被 **封装** 在类的内部

### 02. 小明爱跑步
需求：
1. 小明体重`75.0`公斤
2. 小明每次 **跑步** 会减肥 `0.5`公斤
3. 小明每次 **吃东西** 体重会增加`1` 公斤

<img src="/Users/derek/Library/Application Support/typora-user-images/image-20201010113605969.png" alt="image-20201010113605969" style="zoom:80%;" />

​	提示：在**对象的方法内部**，是可以 **直接访问对象的属性**的

## Lesson 313 面向对象练习2

* 代码实现：

```python
#!/usr/bin/python
# coding:utf-8

class Person:
    def __init__(self, name, weight):
        # self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s,体重是 %.2f" % (self.name, self.weight)

    def run(self):
        print("%s爱跑步" % self.name)
        self.weight -= 0.5
    def eat(self):
        print("%s是吃货" % self.name)
        self.weight += 1


xiaoming = Person("xiaoming", 75.0)

xiaoming.run()
xiaoming.eat()
print(xiaoming)
```



## Lesson 314 面向对象练习3

#### 2.1 小明爱跑步 - - 小美也爱跑步
**需求：**

1. 小明和小美都爱跑步

2. 小明  体重`75.0`公斤

3. 小美  体重`45.0`公斤

4. 每次 **跑步** 会减肥 `0.5`公斤

5. 每次 **吃东西** 体重会增加`1` 公斤

| **Person** |
| :---- |
| name |
|weight|
|\__init__(self, name, weight):|
|\__str__(self):|
|run(self):|
|eat(self):|

**提示**

1. 在对象的方法内部，是可以 **直接访问对象的属性**的

2. **同一个类** 创建的 **多个对象** 之间，**属性** 互不干扰

## Lesson 315 面向对象练习4
### 03. 摆放家具

**需求**

1. 房子(House)有 **户型**、**总面积** 和 **家具名称列表**
   
   * 新房子没有任何的家具
   
2. 家具(HouseItem) 有 **名字** 和 **占地面积**，其中
   
   * **席梦思(bed)** 占地 `4` 平米
   
   * **衣柜(chest)** 占地 `2` 平米
   
   * **餐桌(table)** 占地 `1.5` 平米
   
3. 将以上三件 **家具 添加** 到 **房子**中

4. 打印房子时，要求输出：**户型、总面积、剩余面积、家具名称列表**

   ![image-20201012204609141](/Users/derek/Library/Application Support/typora-user-images/image-20201012204609141.png)

**剩余面积**
1. 在创建房子对象时，定义一个 **剩余面积的属性，初始值和总面积相等**

2. 当调用`add_item`方法，向房间 **添加家具** 时，让剩余面积

**思考**：先开发哪个类
**答案 -- 家具类 **
1. 家具类简单
2. 房子类要使用家具，**被使用的类**，通常先开发



## Lesson 316 面向对象练习5
#### 3.1 创建家具类
## Lesson 317 面向对象练习6
#### 3.2 创建房子类
代码如下：

```python
class HouseItem:
    def __init__(self, vName, vArea):
        self.name = vName
        self.area = vArea

    def __str__(self):
        return "[%s] 占地面积是 [%.1f]平米" % (self.name, self.area)


class House:
    def __init__(self, vHouseType, vArea):
        self.housetype = vHouseType
        self.area = vArea
        # 剩余面积
        self.free_area = self.area
        # 家具列表
        self.item_list = []

    def __str__(self):
        # python能够自动将一对括号内部的代码连接在一起
        return ("户型：%s\n面积：%.2f[剩余面积%.1f]\n家具:%s"
        % (self.housetype, self.area, self.free_area, self.item_list))

    def add_item(self, vItem):
        print("要添加%s\n" % vItem)


# 生成家具
bed = HouseItem("席梦思", 4.0)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
# print(bed)
# print(chest)
# print(table)

# 添加家具
my_home = House("两居室", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
```
**小结**

1. 创建了一个 房子类，使用到`__init__`和`__str__`两个内置方法
2. 准备了一个`add_item`方法 准备添加家具
3. 使用 **房子类** 创建了 **一个房子对象**
4. 让 **房子对象** 调用了三次`add_item`方法，将 **三件家具** 以实参传递到`add_item`内部

## Lesson 318 面向对象练习7
#### 3.3 添加家具
**需求**

* 1. 判断 **家具的面积** 是否 超过剩余面积，如果超过，提示不能添加
* 2. 将 **家具的名称** 追加到 家具名称列表 中
* 3. 用 **房子的剩余面积 - 家具面积**

```python
def add_item(self, vItem):
    print("要添加%s\n" % vItem)
    # 判断家具的面积
    if vItem.area > self.free_area:
        print("%s 的面积太大，无法添加" % vItem.name)
        return
    # 将家具的名称添加到列表中
    self.item_list.append(vItem.name)
    # 计算剩余面积
    self.free_area -= vItem.area
```

#### 3.4 小结

* 主程序只负责创建 **房子**对象和**家具**对象
* 让**房子** 对象调用`add_item`方法 将家具添加到房子中
* 面积计算、剩余面积、家具列表等处理都被**封装**到**房子类的内部**

## Lesson 319 面向对象练习8

### **面向对象封装案例2**

**目标**

* 士兵突击案例

* 身份运算符

**封装**
1. **封装** 是面向对象编程的一大特点
2. 面向对象编程的**第一步** -- 将属性和方法 **封装** 到一个抽象的 **类** 中
3. 外界使用 **类** 创建 对象，然后 让对象调用方法
4. 对象方法的细节 都被 **封装** 在 **类** 的内部
	*一个对象的* **属性** 可以是 **另一个类创建的对象**

### 01.士兵突击
**需求**
1. **士兵** 许三多 有 一个 AK47

2. **士兵** 可以**开火**

3. **枪** 能够 **发射** 子弹

4. **枪** 装填 子弹 - - 增加子弹数量

![image-20201016093914160](/Users/derek/Library/Application Support/typora-user-images/image-20201016093914160.png)



## Lesson 320 面向对象练习9

#### 1.1 开发枪类 
代码开发：hm_14\_士兵突击\_01_枪类

```python
class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.count = 0

    # load bullet
    def add_bullet(self, count):
        self.count += count

    def shoot(self):
        # 判断子弹数量
        if self.count <= 0:
            print("[%s] no bullet , can't fire " % self.model)
            return
        # 发射子弹 -1
        self.count -= 1
        # 提数发射信息
        print("[%s] tututu...[%d]" % (self.model, self.count))

    def __str__(self):
        return "this is a %s,count:[%i]" % (self.model, self.count)


ak47 = Gun("ak47")
ak47.add_bullet(10)
ak47.shoot()
```

## Lesson 321 面向对象练习10
#### 1.2 开发士兵类

​		*假设：每一个士兵都 **没有枪***

**定义没有初始值的属性**

在定义属性时，如果 不知道设置什么初始值，可以设置为 `None`
* `None` **关键字** 表示 **什么都没有**

* 表示一个 **空对象**，**没有方法和属性**，**是一个特殊的常量**

* 可以讲`None`赋值给任何一个变量

`fire`**方法需求**

* 1. 判断是否有枪，没有枪没法冲锋
* 2. 喊一声口号
* 3. 装填子弹
* 4. 射击

```python
class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹的数量
        self.count = 0

    # load bullet
    def add_bullet(self, count):
        self.count += count

    def shoot(self):
        # 判断子弹数量
        if self.count <= 0:
            print("[%s] no bullet , can't fire " % self.model)
            return
        # 发射子弹 -1
        self.count -= 1
        # 提数发射信息
        print("[%s] tututu...[%d]" % (self.model, self.count))

    def __str__(self):
        return "this is a %s,count:[%i]" % (self.model, self.count)


class Soldier:
    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪--新兵没有枪
        self.gun = None

    def fire(self):
        # 判断有没有枪
        if self.gun == None:
            print("[%s] 还没有枪" % self.name)
            return
        # 喊口号
        print("冲啊。。。[%s]" % self.name)
        # 装子弹
        self.gun.add_bullet(50)
        # 发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("ak47")
# ak47.add_bullet(50)
# ak47.shoot()

# 创建士兵
xusanduo = Soldier("许三多")

# 给对象属性赋值，属性已经在类内部定义，初始值None
xusanduo.gun = ak47
xusanduo.fire()

print(xusanduo.gun)
```

**小结**
1. 创建了一个士兵类，使用到内置方法
2. 在定义属性时，如果 不知道设置什么初始值，可以设置为`None`
3. 在 **封装的** 方法内部，还可以让 **自己的 使用其他类创建的对象属性** 调用已经 **封装好的方法**


## Lesson 322 面向对象练习11


## Lesson 323 面向对象练习12
### 02.身份运算符

身份运算符用于 **比较** 两个对象的 **内存地址** 是否一致 - - **是否是对同一个对象的引用**

* 在`Python`中针对`None`比较时，建议使用`is`判断
| **运算符** | **描述** |  **实例** |
|:--|:-----|:-----|
|is|判断两个标识符是不是引用同一个对象|x is y,类似id(x) == id(y)|
|is not|判断两个标识符是不是引用同一个对象|x is not y,类似id(x) != id(y)|

**is 与 == 区别**

`is` 用于判断 **两个变量 引用对象是否为同一个**

`==` 用于判断 **引用变量的值** 是否相等

```python
>>> a = [1,2,3]
>>> b = [1,2,3]
>>> b is a
>>> False
>>> b == a
>>> True
>>>
```
## Lesson 324 面向对象练习13
### 私有属性和私有方法
### 01.应用场景及定义
**应用场景**
* 在实际开发中，**对象** 的 **某些属性或方法** 可能只希望 **在对象的内部被使用，** 而 **不希望在外部被访问到**

* **私有属性** 就是 **对象**  不希望公开的 **属性**

* **私有方法**  就是 **对象**  不希望公开的 **方法**

**定义方法**
* 在 **定义属性或方法时，** 在 **属性名或者方法名前** 增加 **两个下划线**，定义的就是 **私有** 属性或方法

![image-20201017093344007](/Users/derek/Library/Application Support/typora-user-images/image-20201017093344007.png)

```python
class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 [%d]" % (self.name, self.__age))


xiaofang = Women("小芳")
# 私有属性，在外界不能够被直接访问
# print(xiaofang.__age)
# 私有方法，同样不允许在外界被直接访问
# xiaofang.__secret()
```

## Lesson 325 面向对象练习14

### 02.伪私有属性和私有方法（科普）

> _提示：在日常开发中，**不要使用这种方式，访问对象的 私有属性 或 私有方法**_

`python`中，并没有 **真正意义** 的 **私有**

* 在给 **属性、方法** 命名时，实际是对 **名称** 做了一些特殊处理，使得外界无法访问到

* **处理方式：** 在 **名称** 前面加上 `\__类名`=>`\__类名__名称`

```python
# 私有属性，在外界不能够被直接访问
print(xiaofang._Women__age)

# 私有方法，同样不允许在外界被直接访问
xiaofang._Women__secret()
```


## 

## Lesson 326 单继承和方法的重写1

### **继承**
**目标**

* **单继承**

* **多继承**

#### 面向对象三大特性
1. **封装** 根据 **职责** 将 **属性** 和 **方法** **封装** 到一个抽象的 **类** 中
2. **继承** **实现代码的重用，** 相同的代码不需要重复的编写
3. **多态** 不同的对象调用相同的方法，产生不同的执行结果，**增加代码的灵活性**

### 01. 单继承
#### 1.1 继承的概念、语法和特点
**继承的概念：** **子类** 拥有 **父类** 的所有 **方法** 和 **属性**

![image-20201017131835773](/Users/derek/Library/Application Support/typora-user-images/image-20201017131835773.png)



## Lesson 327 单继承和方法的重写2

##### 1) 继承的语法

```python
class 类名(父类名):
		pass
```

* **子类** 继承自 **父类**， 可以直接 **享受** 父类中已经封装好的方法，不需要再次开发
* **子类** 中应该根据 **职责**，封装 **子类特有的 属性和方法**

## Lesson 328 单继承和方法的重写3

##### 2) 专业术语
* `Dog`类是`Animal`类的**子类**，`Animal`类是`Dog`类的**父类**，`Dog`类从`Animal`类**继承**

* `Dog`类是`Animal`类的**派生类**，`Animal`类是`Dog`类的**基类**，`Dog`类从`Animal`类**派生**

## Lesson 329 单继承和方法的重写4
##### 3) 继承的传递性
* `C`类从`B`类继承，`B`类又从`A`类继承
* 那么`C`类就具有`B`类和`A`类的所有属性和方法
**子类** 拥有 **父类** 以及 **父类的父类** 中封装的所有 **属性** 和 **方法**

## Lesson 330 单继承和方法的重写5

**提问**

**啸天犬** 能够调用`Cat`类中定义的`catch`方法吗？

**答案**

**不能**，因为 **啸天犬** 和 `Cat` 之间没有 **继承** 关系

## Lesson 331 单继承和方法的重写6

#### 1.2 方法的重写
* **子类** 拥有 **父类** 的所有 **方法** 和 **属性**

* **子类** 继承自 **父类**，可以直接 **享受** 父类中已经封装好的方法，不需要再次开发
  **应用场景**

* 当 **父类** 的方法实现不能满足子类的需求时，可以对方法进行 **重写(override)**

  

![image-20201017172307139](/Users/derek/Library/Application Support/typora-user-images/image-20201017172307139.png)



**重写** 父类方法有两种情况：

1. **覆盖** 父类的方法

2. 对父类方法进行 **扩展**

##### 1) 覆盖父类的方法

* 如果在开发中，**父类的方法实现** 和 **子类的方法实现，完全不同**
* 就可以使用 **覆盖** 的方式，在**子类中 重写编写** 父类的方法实现
> 具体的实现方式，就相当于在 子类中 定义了一个 和父类同名的方法并且实现

重写之后，在运行时，**只会调用** 子类中重写的方法，而不再会调用 **父类封装的方法**

## Lesson 332 单继承和方法的重写7
##### 2) 对父类方法进行 扩展

* 如果在开发中，**子类的方法实现** 中 **包含** **父类的方法实现**

  * **父类原本封装的方法实现** 是 **子类方法的一部分**

* 就可以使用 **扩展** 的方式
  1. **在子类中 重写** 父类的方法
  
  2. 在需要的位置使用`super().父类方法` 来调用父类方法的执行

  3. 代码其他的位置针对子类的需求，编写 **子类特有的代码实现**
  

**关于 super**

* 在`Python`中，`super`是一个特殊的类
* `super()`就是使用`super`类创建出来的对象
* **最常** 使用的场景就是在**重写父类方法时，** 调用 **在父类中封装的方法实现**

## Lesson 333 单继承和方法的重写8

**调用父类方法的另一种方式（知道**
> *在`Python 2.x`时，如果需要调用父类的方法，还可以使用以下方式：*

```python
父类名.方法(self)
```
* 这种方式，目前在`Python 3.x`还支持这种方式
* 这种方式 **不推荐使用，** 因为一旦 **父类发生变化**， 方法调用位置的 **类名** 同样需要修改
**提示**
* 在开发时，和 两种方式不要混用
* 如果使用 **当前子类名** 调用方法，会形成递归调用，**出现死循环**
## Lesson 334 私有属性和方法1

#### 1.3 父类的 私有属性 和 私有方法
1. **子类对象** 不能 在自己的方法内部， **直接** 访问 弗雷德 **私有属性** 或 **私有方法**
2. **子类对象** 可以通过 **父类** 的 **公有方法** 间接 访问到 **私有属性** 或 **私有方法**
> * **私有属性、方法** 是对象的隐私，不对外公开，**外界** 以及 **子类** 都不能直接访问
> * **私有属性、方法** 通常用于做一些内部的事情

**示例**

![image-20201022153547631](/Users/derek/Library/Application Support/typora-user-images/image-20201022153547631.png)

* `B`的对象不能直接访问 `__num2` 属性
* `B`的对象不能在 `demo` 方法内部访问`__num2` 属性
* `B`的对象可以在`demo` 方法内，调用父类的`test`方法
* 父类的`test`方法内部，能够访问`__num2` 属性和`__test`方法

## Lesson 335 私有属性和方法2
* 本节笔记与上节相同
## Lesson 336 多继承1

### 02.多继承

* **子类** 可以拥有 **多个父类**，并且具有 **所有父类** 的 **属性** 和 **方法**

* 例如：**孩子** 会继承自己 **父亲** 和 **母亲** 的 **特性**

<img src="/Users/derek/Library/Application Support/typora-user-images/image-20201022215832730.png" alt="image-20201022215832730" style="zoom:50%;" />



**语法**

```python
class 子类名(父类名1,父类名2):
		pass
```

## Lesson 337 多继承2

#### 2.1 多继承的使用注意事项
**问题的提出**
* 如果 **不同的父类** 中存在 **同名的方法，子类的对象** 在调用方法时，会调用 **哪一个父类中** 的方法呢？
> 提示：**开发时，应该尽量避免这种容易产生混淆的情况！** ---- 如果 **父类之间** 存在 **同名的属性或者方法，** 应该 **尽量避免** 使用多继承

jfkdjfdk

![image-20201024180542942](/Users/derek/Library/Application Support/typora-user-images/image-20201024180542942.png)



## Lesson 338 多继承3

**科普**

##### **Python 重的 MRO ---- 方法搜索顺序（知道）**

* `Python`中针对 **类** 提供了一个 **内置属性** `__mro__`可以查看 **方法** 搜索顺序
* MRO 是 `method resolution order`, 主要用于 **在多继承时判断 方法、属性 的调用 路径
```python
	print(C.__mro__)
```
输出结果：
```
	(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

* 在搜索方法时，是按照 的输出结果 **从左至右** 的顺序查找的
* 如果在当前类中 **找到方法，就直接执行，不再搜索**
* 如果 **没有找到，就查找下一个类** 中是否有对应的方法，**如果找到，就直接执行，不再搜索**
* 如果找到最后一个类，还没有找到方法，程序报错



## Lesson 339 多继承4

#### 2.2 新式类与旧式（经典）类

> `object`是`Python`为所有对象提供的**基类**， 提供有一些内置的属性和方法，可以使用`dir`函数查看

* **新式类**：以`object`为基类的类，**推荐使用**

* **经典类**：不以`object`为基类的类，**不推荐使用**

* 在`Python 3.x`中定义类时，如果没有指定父类，会 **默认使用** `object`作为该类的 **基类** ---- `Python 3.x`中定义的类都是 **新式类**

* 在`Python 2.x`中定义类时，如果没有指定父类， 则不会以 `object`作为 **基类**

> **新式类** 和 **经典类** 在多继承时 ---- **会影响到方法的搜索顺序**

为了保证编写的代码能够同时在`Python 3.x`和`Python 2.x`运行
今后在定义类时，**如果没有父类，建议同意继承自 `object`**

```python
class 类名(object):
  	pass
```

**新式类：** python 3.7中

```python
In [1]: class A:
   ...:     pass
   ...:

In [2]:

In [2]: a = A()

In [3]: dir(a)
Out[3]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']

```

**经典类** python 2.x中：
```python
>>> class A:
>>> ...     pass
>>> ...
>>> a = A()
>>> dir(a)
>>> ['__doc__', '__module__']
>>>
```


## Lesson 340 多态基本概念

### 多态
**目标**
* 多态
**面向对象的三大特性**
1. **封装** 根据 **职责** 将 **属性** 和 **方法 封装** 到一个抽象的 **类** 中
   
   * 定义类的准则
2. **继承 实现代码的重用**，相同的代码不需要重复的编写
   * 设计类的技巧
   * 子类针对自己特有的需求，编写特定的代码
3. **多态** 不同的 **子类对象** 调用相同的 **父类方法**，产生不同的执行效果
   * **多态** 可以 **增加代码的灵活度**
   
   * 以 **继承** 和 **重写父类方法** 为前提
   
   * 是调用方法的技巧，**不会影响到类的内部设计**
   

![image-20201024221950593](/Users/derek/Library/Application Support/typora-user-images/image-20201024221950593.png)



## Lesson 341 多态案例演练

### 多态案例演练
**需求**
1. 在`Dog`类中封装方法`game`
   
    * 普通狗只是简单的玩耍
2. 定义`Xiaotianquan`继承自`Dog`，并且重写`game`方法
   
    * 啸天犬 需要在天上玩耍
3. 定义`Person`类，并且封装一个 **和狗玩**的方法
   
    * 在方法内部，直接让 **狗对象** 调用`game`方法
    

![image-20201024222632114](/Users/derek/Library/Application Support/typora-user-images/image-20201024222632114.png)

**案例小结**

* `Person`类中只需要让 **狗对象** 调用 `game`方法，而不关系具体是 **什么狗**

  * `game`方法是`Dog`父类中定义的

* 在执行程序时，传入不同的 **狗对象** 实参，就会产生不同的执行效果

## Lesson 342 类属性1

### 01. 类的结构
#### 1.1 术语 ---- 实例
1. 使用面向对象开发，**第一步** 是 设计 **类**

2. 使用 **类名()** 创建对象，**创建对象** 的动作有两步：
	* 1）在内存中为对象 **分配空间**
	* 2）调用初始化方法 `__init__` 为 **对象初始化**
	
3. 对象创建后，**内存** 中就有了一个对象的**实实在在** 的存在 ---- **实例**

![image-20201024224358242](/Users/derek/Library/Application Support/typora-user-images/image-20201024224358242.png)

因此，通常也会把：

1. 创建出来的 **对象** 叫做 **类** 的 实例

2. 创建对象的 **动作** 叫做 实例化

3. **对象的属性** 叫做 **实例属性**

在程序设计时：
1. 对象各自拥有自己的 **实例属性**
2. 调用对象方法，可以通过`self.`
    * 访问自己的属性
    * 调用自己的方法
**总结**
* **每一个对象** 都有自己 **独立的内存空间，保存各自不同的属性 **
* **多个对象的方法，在内存中只有一份，** 在调用方法时，**需要把对象的引用** 传递到方法内部
## Lesson 343 类属性2
#### 1.2 类是一个特殊的对象

> `Python`中 **一切皆对象**
>
> * `class AAA:` 定义的类属于 **类对象**
> * `obj1 = AAA()` 属于 **实例对象**

* 在程序运行时，**类** 同样 **会被加载到内存**
* 在`Python`中，**类** 是一个特殊的对象 ---- **类对象**
* 在程序运行时，**类对象** 在内存中 **只有一份** ，使用 **一个类** 可以创建出 **很多个对象实例**
* 除了封装 **实例** 的 **属性** 和 **方法** 外，**类对象** 还可以拥有自己的 **属性** 和 **方法**
	1. **类属性
	2. 类方法**
* 通过 **类名. ** 的方式可以 **访问类的属性** 或者 **调用类的方法**

![image-20201025132323369](/Users/derek/Library/Application Support/typora-user-images/image-20201025132323369.png)



## Lesson 344 类属性3

### 02. 类属性和实例属性
#### 2.1 概念和使用
* **类属性** 就是给 **类对象** 中定义的 **属性**
* 通常用来记录 **与这个类相关** 的特征
* **类属性 不会用于** 记录 **具体对象的特征**

**示例需求**
* 定义一个 **工具类**
* 每件工具都有自己的`name`
* **需求** ---- 知道使用这个类，创建了多少个工具对象？

![image-20201025175906266](/Users/derek/Library/Application Support/typora-user-images/image-20201025175906266.png)

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0
    
    def __init__(self, name):
        self.name = name
        # 让类属性+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
# 输出工具对象的总数
print(Tool.count)
```

## Lesson 345 类属性4

#### 2.2 属性的获取机制（科普）
* 在`Python`中 属性的获取 存在一个 **向上检查机制**

![image-20201025212423407](/Users/derek/Library/Application Support/typora-user-images/image-20201025212423407.png)

* 因此，要访问类属性有两种方式：
  1. **类名.类属性**
  2. **对象.类属性** （不推荐)

**注意**

* 如果使用`对象.类属性 = 值`赋值语句，只会 **给对象添加一个属性**，而不会影响到 **类属性的值**

## Lesson 346 类属性5

***对象.类属性 读取 类属性的值没有问题，但设置值时，会在对象内部添加一个对象属性，而不会改变类对象的值 从而造成混淆***

## Lesson 347 类方法1

### 03. 类方法和静态方法
#### 3.1 类方法

* **类属性** 就是针对 **类对象** 定义的属性
  * 使用 **赋值语句** 在`class`关键字下方可以定义 **类属性**
  * **类属性** 用于记录 **与这个类相关** 的特征
* **类方法** 就是针对 **类对象** 定义的方法
  * 在 **类方法** 内部可以直接访问 **类属性** 或者调用其他的 **类方法**

**语法如下**

```python
@classmethod
def 类方法名(cls):
  pass
```

* 类方法需要用 **修饰器** `@classmethod`来标识，**告诉解释器这是一个类方法**
* 类方法的 **第一个参数** 应该是`cls`
  *  由 **哪一个类** 调用的方法，方法内的`cls`就是 哪一个类的引用
  * 这个参数和 **实例方法** 的第一个参数是 `self`类似
  * **提示** 使用其他名称也可以，不过习惯使用`cls`
* 通过 **类名**，调用 **类方法 调用类方法时**，不需要传递`cls`参数
* **在方法内部**
  * 可以通过`cls.` **访问类的属性**
  * 也可以通过`cls`，**调用其他的类方法**

## Lesson 348 类方法2

**示例需求**

* 定义一个工具类
* 每件工具都有自己的`name`
* **需求** ---- 在 **类** 封装一个 `show_tool_count` 的类方法，输出使用当前这个类，创建的对象个数



![image-20201026100625592](/Users/derek/Library/Application Support/typora-user-images/image-20201026100625592.png)



```python
@classmethod
def show_tool_count(cls):
    # 现实工具对象的总数
    print("工具对象的数量：%d" % cls.count)
```

> *在类方法内部，可以直接使用`cls` 访问 **类属性** 或者 **调用类方法***

## Lesson 349 静态方法的场景和定义方式

#### 3.2 静态方法

* 在开发时，如果需要在 **类** 中封装一个方法，这个方法：
  * 既 **不需要** 访问 **实例属性** 或者调用 **实例方法**
  * 也 **不需要** 访问 **类属性** 或者调用 **类方法**
* 这个时候，可以把这个方法封装成一个 **静态方法**

**语法如下：**

```python
@staticmethod
def 静态方法名():
  pass
```

* **静态方法** 需要用 **修饰器** `@staticmethod`来标识，告诉**解释器这是一个静态方法**
* 通过 **类名**，调用 **静态方法**

```python
class Dog(object):

    @staticmethod
    def run():
        # 不访问 实例属性/类属性
        print("小狗要跑")

    def __init__(self, name):
        self.name = name


# 通过 类名. 的方式调用静态方法 - 不需要创建对象
Dog.run()
```

## Lesson 350 方法综合练习1

#### 3.3 方法综合案例
**需求** 
1. 设计一个`Game`类

2. 属性：
	
	* 定义一个 **属性类** `top_score` 记录游戏的 **历史最高得分**
	* 定义一个 **实例属性** `player_name` 记录 当前游戏的玩家姓名
	
3. 方法：

   * **静态方法** `show_help`显示游戏帮助信息
   * **类方法** `show_top_score` 显示历史最高分
   * **实例方法** `start_game` 开始当前玩家的游戏

4. 主程序步骤

   * 1）查看帮助信息
   * 2）查看历史最高分
   * 3）创建游戏对象，开始游戏

   ![image-20201027094735007](/Users/derek/Library/Application Support/typora-user-images/image-20201027094735007.png)

   

## Lesson 351 方法综合练习2

**hm_17_方法综合案例：**

```python
class Game(object):
    # 定义类属性历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息：XXXX")

    @classmethod
    def show_top_score(cls):
        print("历史记录：%d" % cls.top_score)

    def start_game(self):
        print("%s 开始游戏..." % self.player_name)


# 1. 查看游戏帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()

# 3. 创建游戏对象
game1 = Game("小明")
game1.start_game()
```



## Lesson 352 单例设计模式1

### 单例
**目标**

* 单例设计模式
* `__new__`方法
* Python中的单例

### 01. 单例设计模式

* **设计模式**
  * **设计模式** 是 **前人工作的总结和提炼**，通常，被人们广泛流传的设计模式都是针对 **某一特定问题** 的成熟的解决方案
  * 使用 **设计模式** 是为了可重用代码，让代码更容易被他人理解，保证代码可靠性
* **单例设计模式**
  * **目的** ---- 让 **类** 创建的对象，在系统中 **只有 唯一的一个实例**
  * 每一次执行 `类名()` 返回的对象，**内存地址是相同的**

**单例设计模式的应用场景**

* **音乐播放** 对象
* **回收站** 对象
* **打印机** 对象
* **.......**



## Lesson 353 单例设计模式2

### 02. `__new__`方法

* 使用 **类名()** 创建对象时，`Python` 的解释器 **首先** 会 调用 `__new__`方法为对象 **分配空间**

* `__new__` 是一个由 `object` 基类提供的 **内置的静态方法** ，主要左右有两个：

  * 在内存中为对象 **分配空间**
  * **返回** 对象的引用

* `Python` 的解释器获得对象的 **引用** 后，将引用作为 **第一个参数** ， 传递给 `__init__`方法

  > *重写 `__new__` 方法的代码非常固定*

* 重写 `__new__` 方法 **一定要**`return super().__new__(cls)`

* 否则`Python` 的解释器 **得不到** 分配了空间的 **对象引用** ，**就不会调用对象的初始化方法**

* 注意：`__new__` 是一个静态方法，在调用时需要 **主动传递`cls`参数**

![image-20201027104736662](/Users/derek/Library/Application Support/typora-user-images/image-20201027104736662.png)



## Lesson 354 单例设计模式3

**hm_18\__new__方法**

```python
class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 1.使用类名创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 2.为对象分配空间
        instance = super().__new__(cls)
        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
```

## Lesson 355 单例设计模式4

### 03.Python中的单例
* 单例 ---- 让 **类** 创建的对象，在系统中 **只有 唯一的一个实例**
  1. 定义一个 **类属性** ，初始值是`None`，用于记录 **单例对象的引用**
  2. 重写 `__new__`方法
  3. 如果 **类属性** `is None`，调用父类方法分配空间，并在类属性中记录结果
  4. 返回 **类属性** 中记录的 **对象引用**

![image-20201027113146720](/Users/derek/Library/Application Support/typora-user-images/image-20201027113146720.png)





## Lesson 356 单例设计模式5

hm_19_单例:

```python
class MusicPlayer(object):
    # 定义类属性，记录第一个单例对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回保存的类属性对象引用
        return cls.instance

    def __init__(self):
        print("初始化")


# 创建三次实例，查看引用是否相同
for i in range(3):
    player1 = MusicPlayer()
    print("第[%d]次: %s" % (i+1, player1))
```

## Lesson 357 单例设计模式6

### 只执行一次初始化工作

* 在每次使用 `类名（）`创建对象时，`Python`的解释器都会自动调用两个方法：
  * `__new__`分配空间
  * `__init__`对象初始化
* 在上一小节对`__new__`方法改造之后，每次都会得倒 **第一次被创建对象的引用**
* 但是：**初始化方法还会被再次调用**

**需求**

* 让 **初始化动作** 只被 **执行一次**

**解决办法**

1. 定义一个类属性 `init_flag` 标记是否 **执行过初始化动作**，初始值为`False`
2. 在`__init__`方法中，判断`init_flag`, 如果为`False` 就执行初始化动作
3. 然后将`init_flag`设置为`True`
4. 这样，再次 **自动 调用** `__init__`方法时，**初始化动作就不会被再次执行**

```python
class MusicPlayer(object):
    # 定义类属性，记录第一个单例对象的引用
    instance = None
    init_count = 0
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 返回保存的类属性对象引用
        return cls.instance

    def __init__(self):
        # 判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 如果没有执行过，执行初始化动作
        print("初始化")
        MusicPlayer.init_count += 1
        # 修改类属性标记
        MusicPlayer.init_flag = True

    @classmethod
    def show_init_times(cls):
        print(cls.init_count)


# 创建三次实例，查看引用是否相同
for i in range(3):
    player1 = MusicPlayer()
    print("第[%d]次创建对象: %s" % (i + 1, player1))

# 查看初始化方法被调用的次数
MusicPlayer.show_init_times()
```



## Lesson 358 异常的概念和抛出异常原因

### 异常

**目标**

* 异常的概念
* 捕获异常
* 异常的传递
* 自定义异常

### 01. 异常的概念

* 程序在运行时，如果`Python解释器` **遇到** 一个错误，**会停止程序的执行，并且提示一些错误信息**。                  这就是 **异常**
* **程序停止执行并且提示错误信息** 这个动作，我们通常称之为：**抛出(raise)异常**

![image-20201027143156680](/Users/derek/Library/Application Support/typora-user-images/image-20201027143156680.png)

> *程序开发时，很难将 **所有的特殊情况** 都处理的面面俱到，通过 **异常捕获** 可以针对突发事件做集中的处理，从而保证程序的 **稳定性和健壮性***

## Lesson 359 简单的异常捕获

### 02. 简单的捕获异常语法

#### 2.1 简单的捕获异常语法

* 在程序开发中，如果 **对某些代码的执行不能确定是否正确** 可以增加 `try(尝试)`来 **捕获异常**
* 捕获异常最简单的语法格式：

```Python
try:
  尝试执行的代码
except:
  出现错误的处理
```

* `try`**尝试**，下方编写要尝试代码，不确定是否能够正常执行的代码
* `except`**如果不是**，下方编写尝试失败的代码

**简单异常捕获演练 ---- 要求用户输入整数**

```python
# 提示用户输入一个整数
try:
    num = int(input("请输入一个整数: "))
except:
    # 错误处理代码
    print("请输入正确的整数")

print("-" * 50)
```

## Lesson 360 根据错误类型捕获异常

#### 2.2 错误类型捕获

* 在程序执行时，可能会遇到 **不同类型的异常**，并且需要 **针对不同类型的异常，做出不同的响应**，这个时候，就需要捕获错误类型了
* 语法如下：

```python
try:
  # 尝试执行的代码
  pass
except 错误类型1:
  # 针对错误类型1，对应的代码处理
  pass
except(错误类型2，错误类型3):
  # 针对错误类型2 和 3，对应的代码处理
  pass
except Exceptions as result:
  print("未知错误 %s" % result)
```

* 当`Python`解释器 **抛出异常** 时，**最后一行错误信息的第一个单词，就是错误类型**

**异常类型捕获演练 ---- 要求用户输入整数**

**需求**

1. 提示用户输入一个整数
2. 使用`8`除以用户输入的整数并且输出

```python
try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 使用`8`除以用户输入的整数并且输出
    result = 8 / num
    print("输入的整数是 [%d]" % result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("非数字错误")
```

## Lesson 361 捕获未知错误

**捕获未知错误**

* 在开发时，**要预测到所有可能出现的错误，**还是有一定难度的
* 如果希望程序 **无论出现任何错误**，都不会因为`Python`解释器 **抛出异常而被终止**，可以再增加一个`except`

**语法如下**
```Python
except Exceptions as result:
  print("未知错误 %s" % result)
```

## Lesson 362 异常捕获的完整语法

#### 2.3 异常捕获完整语法

* 在实际开发中，为了能够处理复杂的异常情况，完整的异常语法如下：

> *提示：*
>
> * 有关完整语法的应用场景，在后续学习中，**结合实际的案例**会更好理解
> * 现在对这个语法结构有印象即可



```python
try:
  # 尝试执行的代码
  pass
except 错误类型1:
  # 针对错误类型1,对应的代码处理
  pass
except 错误类型2:
  # 针对错误类型2,对应的代码处理
  pass
except (错误类型3, 错误类型4):
  # 针对错误类型3 和 4,对应的代码处理
  pass
except Exceptions as result:
  # 打印错误信息
  print("未知错误 %s" % result)
else:
  # 没有异常才会执行的代码
  pass
finally:
  # 无论如何都会执行的代码
  print("无论是否有异常，都要执行")
```



* `else`只有在没有异常时才会执行的代码

* `finally`无论是否有异常，都会执行的代码

* 之前一个演练的 **完整捕获异常** 的代码如下：

```python
try:
    # 1. 提示用户输入一个整数
    num = int(input("请输入一个整数："))

    # 2. 使用`8`除以用户输入的整数并且输出
    result = 8 / num
    # if result == 0:
    print("输入的整数是 [%d]" % result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("非数字错误")
except Exception as err:
    print("未知错误 [%s]" % err)
else:
    print("尝试成功！")
finally:
    print("无论是否出现错误都会执行！")

print("-" * 50)
```

## Lesson 363 异常的传递性

### 03. 异常的传递

* **异常的传递** ---- 当 **函数/方法** 执行 **出现异常，** 会 **将异常传递** 给 函数/方法 的 **调用一方**
* 如果 **传递到主程序**，仍然 **没有异常处理**，程序才会被终止

> *提示*

* 在开发中，可以在主函数中增加 **异常捕获**
* 而在主函数中调用的其他函数，只要出现异常，都会传递到主函数的 **异常捕获**中
* 这样就不需要在代码中，增加大量的 **异常捕获** ，能够保证代码的整洁

**需求**

1. 定义函数`demo1()`**提示用户输入一个整数并返回**
2. 定义函数`demo2()` 调用`demo1()`
3. 在主程序中调用`demo2()`

```python
def demo1():
    return int(input("请输入一个整数："))


def demo2():
    return demo1()


try:
    demo2()
except ValueError:
    print("不是一个整数")
except Exception as result:
    print("未知错误 [%s]" % result)
else:
    pass
finally:
    print("-" * 50)
```

## Lesson 364 主动抛出异常的应用场景

### 04. 抛出raise异常

#### 4.1 应用场景

* 在开发中，除了 **代码执行出错** `Python`解释器会 **抛出** 异常之外
* 还可以根据 **应用程序 特有的业务需求 主动抛出异常**

**示例**

* 提示用户 **输入密码，** 如果 **长度少于8，** 抛出 **异常**

![image-20201028151549662](/Users/derek/Library/Application Support/typora-user-images/image-20201028151549662.png)

**注意**

* 当前函数 **只负责** 提示用户输入密码，如果 **密码长度不正确，需要其他的函数进行额外处理**
* 因此可以 **抛出异常**，由其他需要处理的函数 **捕获异常**



## Lesson 365 主动抛出异常案例演练

#### 4.2 抛出异常

* `Python`中提供了一个`Exception` **异常类**
* 在开发中，如果满足 **特定业务需求时，** 希望 **抛出异常**，可以：

       1. **创建**一个`Exception` 的 **对象**
          2. 使用`raise` **关键字** 抛出 **异常对象**

**需求**

* 定义 `input_password` 函数，提示用户输入密码
* 如果用户输入长度长度 < 8,抛出异常
* 如果用户输入长度 >= 8, 返回输入的密码

```python
def input_password():
    # . 提示用户输入密码
    pwd = input("请输入密码：")
    # . 判断密码长度，够8位返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # . 不够8位，主动抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
```

## Lesson 366 模块概念和import导入复习

* 包
* 模块的制作

### 01. 模块

#### 1.1 模块的概念

> ***模块时Python程序架构的一个核心概念***

* 每一个以拓展名`py`结尾的 `Python`源代码文件都是一个 **模块**
* **模块名** 同样也是一个 **标识符** ，需要符合标识符的命名规则
* 在模块中定义的 **全量变量、函数、类** 都是提供给外界直接使用的 **工具**
* **模块** 就好比是 **工具包** ，要使用这个工具包的工具，就需要先 **导入** 这个模块

#### 1.2 模块的两种导入方式

1. **import导入**

```python
import 模块名1，模块名2
```

> *提示：在导入模块时，每个导入应该独占一行*

```python
import 模块名1
import 模块名2
```

* **导入之后**
  * 通过 `模块名.`使用 **模块提供的工具 ---- 全局变量、函数、类**

## Lesson 367 import导入时指定别名

**使用as指定模块的别名**

> ***如果模块的名字太长，**，可以使用`as`指定模块的名称，以方便在代码中使用*

```python
import 模块名1 as 模块别名
```

>  *注意：**模块别名** 应该符合**大驼峰命名法***

2. from import 导入

* 如果希望 **从某一个模块** 中，导入 **部分** 工具，就可以使用`from ... import`的方式
* `import 模块名`是 一次性 把模块中 **所有工具全部导入**，并且通过 **模块名/别名** 访问

```python
# 从 模块 导入 某一个工具
from 模块名1 import 工具名
```

* 导入之后
  * **不需要** 通过 `模块名.`
  * 可以直接使用 **模块提供的工具 ---- 全局变量、函数、类**

## Lesson 368 from import局部导入

```python
from hm_01_测试模块1 import Dog
from hm_02_测试模块2 import say_hello


say_hello()
wangcai = Dog()
print(wangcai)
```

## Lesson 369 from import导入同名工具

**注意**

> *如果**两个模块**，存在 **同名** 的 **函数**， 那么 **后导入模块的函数**，会 **覆盖掉先导入的函数***

* 开发时 `import`代码应该统一写在 **代码的顶部**，更容易及时发现冲突
* 一旦发现冲突，可以以用`as` 关键字 **给其中一个工具起一个别名**

```python
from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as module2_say_hello

say_hello()
module2_say_hello()
```

## Lesson 370 导入所有工具

**from_import * (知道)**

```python
# 从 模块 导入所有工具
from 模块名1 import *
```

**注意**

> *这种方式不推荐使用，因为函数重名并没有任何的提示，出现问题不好排查*

## Lesson 371 模块搜索顺序

#### 1.3 模块的搜索顺序[扩展]

`Python`的解释器在 **导入模块** 时，会：

1. 搜索 **当前目录** 指定模块名的文件，**如果有就直接导入**
2. 如果没有，再搜索 **系统目录**

> ***在开发时，给文件起名，不要和 系统的模块文件 重名***

`Python`中每一个模块都有一个内置属性`__file__`可以 **查看模块**的 **完整路径**

**示例**

```python
import random
# 生成一个 0～10的数字
rand = random.randint(0,10)
print(rand)
```

> *注意：如果当前目录下，存在一个`random.py`的文件，程序就无法正常运行了*

* 这个时候，`Python` 的解释器会 **加载当前目录** 下的 `random.py` 而不会加载 **系统的** `random`模块

## Lesson 372 会执行没有缩进的代码

#### 1.4 原则 —— 每一个文件都应该是可以被导入的

* 一个 **独立的** `Python`文件 就是一个 **模块**
* 在导入文件时，文件中 **所有没有任何缩进的代码** 都会被执行一遍

**实际开发场景**

* 在实际开发中，每一个模块都是独立开发的，大多都有专人负责
* **开发人员** 通常会在 **模块下方 增加一些测试代码**
  * 仅在模块内使用，而被导入到其他问家中不需要执行



## Lesson 373 `__name__`属性导入两种模式

**\__name__属性**

> * `__name__`属性可以做到，测试模块的代码 **只在测试情况下被运行，** 而在 **被导入时不会被执行**

* `__name__`是`Python`的一个内置属性，记录着一个 **字符串**

* 如果 **是被其他文件导入的，** `__name__`就是 **模块名**
* 如果 **是当前执行的程序** `__name__` 是 **`__main__`**

**在很多`Python`文件中都会看到如下格式的代码：**

```python
# 导入模块
# 定义全局变量
# 定义类
# 定义函数

#在代码最下方
def main():
  # ...
  pass

# 根据 __name__ 判断是否执行下方代码：
if __name__ == "__main__":
  main()
```



## Lesson 374 包的概念以及建立包的方式

### 02. 包(Package)

**概念**

* **包** 是一个 **包含多个模块** 的 **特殊目录**
* 目录下有一个 **特殊的文件** `__init__.py`
* 包名的 **命名方式** 和变量名一致，**小写字母 + _**

**好处**

* 使用`import 包名`可以一次性导入 **包** 中 **所有的模块**

**案例演练**

1. 新建一个`hm_message`的 **包**
2. 在目录下，新建两个文件 `send_message`和 `receive_message`
3. 在 `send_message`文件中定义一个`send`函数
4. 在 `receive_message`文件中定义一个`reseive`函数
5. 在外部直接导入`hm_message`的包

\_**_init__.py**

* 要在外界使用 **包** 中的模块，需要在 `__init__.py`中指定 **对外界提供的模块列表**

```python
# 从 当前目录 导入 模块列表
from . import send_message
from . import receive_message
```



## Lesson 375 封装模块设置和外界导入包



## Lesson 376 制作模块目的和介绍步骤

### 03. 发布模块（知道）

* 如果希望自己开发的模块 **分享** 给其他人，可以按照以下步骤操作

#### 3.1 制作发布压缩包步骤

1. **创建 setup.py**

* `setup.py` 的文件：



## Lesson 377 制作模块压缩包



## Lesson 378 安装模块压缩包



## Lesson 379 卸载已经安装过的模块



## Lesson 380 使用pip安装pygame模块



## Lesson 381 文件操作1

**目标**

* 文件的概念
* 文件的基本操作
* 文件/文件夹的常用操作
* 文本文件的编码方式

### 01. 文件的概念

#### 1.1 文件的概念和作用

* 计算机中的 **文件** 就是存储在某种 **长期存储设备** 上的一段 **数据**
* 长期存储设备包括：硬盘、U盘、移动硬盘、光盘。。。

**![image-20201030103520448](/Users/derek/Library/Application Support/typora-user-images/image-20201030103520448.png)**



**文件的作用**

将数据长期保存下来，在需要时使用

#### 1.2 文件的存储方式

* 在计算机中，文件是以**二进制**的方式保存在磁盘上的

**文本文件和二进制文件**

* 文本文件
  * 可以使用 **文本编辑软件** 查看
  * 本质上还是二进制文件
  * 例如：Python 的源程序
* 二进制文件
  * 保存的内容 不是给人直接阅读的，而是 **提供给其他软件使用的**
  * 例如：图片文件、音频文件、视频文件等等
  * 二进制文件不能使用 **文本编辑软件** 查看

## Lesson 382 文件操作2

### 02. 文件的基本操作

#### 2.1 操作文件的套路

在 **计算机** 中要操作文件的套路非常固定，一共包含三个步骤：

1. 打开文件
2. 读、写文件
   * 读 将文件内容读入内存
   * 写 将内存内容写入文件
3. 关闭文件

#### 2.2 操作文件的函数/方式

* 在`Python`中要操作文件需要记住1个函数和3个方法

| **序号** |**函数/方法** |**说明**                       |
| :--------- | |:----------------------------- |
| 01     | open |打开文件，并且返回文件操作对象 |
| 02        | read |将文件内容读取到内存      |
| 03       | write |将指定内容写入文件 |
| 04     | close |关闭文件            |

* `open`函数负责打开文件，并且返回文件对象
* `read/write/close`三个方法都需要通过 **文件对象** 来调用

## Lesson 383 文件操作3

#### 2.3 read方法 —— 读取文件

* `open`函数的第一个参数是要打开的文件名 (文件名区分大小写)
  * 如果文件 **存在** ，返回 **文件操作对象**
  * 如果文件 **不存在** 会 **抛出异常**
* `read`方法可以一次性 **读入** 并 **返回** 文件的 **所有内容**
* `close`方法负责 **关闭文件**
  * 如果 **忘记关闭文件**，**会造成系统资源消耗，并且会影响到后续对文件的访问**
* **注意**：方法执行后，会把 **文件指针** 移动到 **文件的末尾**

```python
# 1. 打开 —— 文件名需要注意大小写
file = open("README")
# 2. 读取
text = file.read()
print(text)
# 3. 关闭
file.close()
```

**提示**

* 在开发中，通常会先编写 **打开** 和 **关闭** 的代码，再编写中间针对文件的 **读/写** 操作

## Lesson 384 文件操作4

**文件指针（知道）**

* **文件指针** 标记 **从哪个位置开始读取数据**
* **第一次打开** 文件时，通常 **文件指针会指向文件的开始位置**
* 当执行了 `read`方法后，**文件指针** 会移动到 **读取内容的末尾**
  * 默认情况下会移动到 **文件末尾**

**思考**

* 如果执行了一次`read`方法，读取了所有内容，那么再次调用`read`方法，还能够获得内容么？

## Lesson 385 文件操作5

#### 2.4 打开文件的方式

* `open`函数默认以 **只读方式** 打开文件，并且返回文件对象

**语法如下：**

```python
f = open("filename","访问方式")
```

|访问方式|说明|
|:-----:|:----------------------------|
|r|以 **只读** 方式打开文件。文件的指针将会放在文件的开头，这是 **默认模式** 。如果文件不存在，抛出异常|
|w|以 **只写** 方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件|
|a|以 **追加** 方式打开文件。如果该文件存在，文件指针会放在文件的结尾。如果文件不存在，创建新文件进行写入|
|r+|以 **读写** 方式打开文件。文件的指针将会放在文件的开头， 如果文件不存在，抛出异常|
|w+|以 **读写** 方式打开文件。如果文件存在会被覆盖。如果文件不存在，创建新文件|
|a+|以 **读写** 方式打开文件。如果该文件存在，文件指针会放在文件的结尾。如果文件不存在，创建新文件进行写入|

**提示**

* 频繁的移动文件指针，**会影响文件的读写效率**，在开发中更多的时候会以 **只读、只写** 的方式来操作文件

## Lesson 386 文件操作6

#### 2.5 readline 方法

* `read`方法默认会把文件的 **所有内容一次性读取到内存**
* 如果文件太大，对内存的占用会非常严重

**readline方法**

* `readline`方法可以一次读取一行内容
* 方法执行后，会把 **文件指针** 移动到下一行，准备再次读取

**读取大文件的正确姿势**

```python
file = open("README1")

while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)

file.close()
```



## Lesson 387 文件操作7

#### 2.6 文件读写案例 —— 复制文件

**目标**

用代码的方式，来实现文件复制过程

![image-20201102105805492](/Users/derek/Library/Application Support/typora-user-images/image-20201102105805492.png)

**小文件复制**

* 打开一个已有文件，读取完整内容，并写入到另外一个文件

```python
# 1.打开
source_file = open("README1")
target_file = open("README2", "w")
# 2.读、写
text = source_file.read()
target_file.write(text)

# 3.关闭文件
source_file.close()
target_file.close()
```

## Lesson 388 文件操作8

**大文件复制**

* 打开一个已有文件，逐行读取内容，并顺序写入一个文件

```python
# 1.打开
source_file = open("README1")
target_file = open("README2", "w")
# 2.读、写
while True:
    # 按行读取文件
    text = source_file.readline()
    # 判断是否读取到内容
    if not text:
        break
    target_file.write(text)

# 3.关闭文件
source_file.close()
target_file.close()
```

## Lesson 389 文件操作9

### 03.文件/目录的常用管理操作

* 在 **终端/文件浏览器** 中可以执行常规的 **文件/目录** 管理操作，例如：
  * 创建、重命名、删除、改变路径、查看目录内容
* 在`Python`中，如果希望通过程序实现上述功能，需要导入`os`模块

**文件操作**

|序号|方法名|说明|示例|
|:------:|:------:|:----------|:-----------|
|01|rename|重命名文件|os.rename(源文件名,目标文件名)|
|02|remove|删除文件|os.remove(文件名)|

**目录操作**

|序号|方法名|说明|示例|
|:------:|:------:|:----------|:-----------|
|01|listdir|目录列表|os.listdir(目录名)|
|02|mkdir|创建目录|os.mkdir(目录名)|
|03|rmdir|删除目录|os.rmdir(目录名)|
|04|getcwd|获取当前目录|os.getcwd()|
|05|chdir|修改工作目录|os.chdir(目标目录)|
|06|path.isdir|判断是否是文件|os.path.isdir(文件路径)|

> *提示：文件或者目录操作都支持 **相对路径** 和 **绝对路径***

## Lesson 390 文本编码1

### 04.文本文件的编码格式（科普）

* 文本文件 存储的内容是基于 **字符编码** 的文件，常见的编码有 `ASCII`编码，`Unicode`编码等

> *Python 2.x 默认使用`ASCII`编码*
>
> *Python 3.x 默认使用`Unicode`编码*

#### 4.1 ASCII 编码和 Unicode编码

 **ASCII 编码**

* 计算机中只有 `256`个 `ASCII`字符
* 一个 `ASCII`在内存中占用 **1个字节** 的空间
  * `8`个 `0/1`的排列组合方式一共有`256`种，也就是`2**8`

![image-20201102151039723](/Users/derek/Library/Application Support/typora-user-images/image-20201102151039723.png)



**UTF-8编码格式**

* 计算机中使用 **1-6个字节** 来表示一个`UTF-8`字符，涵盖了 **几乎所有地区的文字**
* 大多数汉字会使用 **3个字节** 表示
* `UTF-8` 是`Unicode` 编码的一种编码格式



## Lesson 391 文本编码2

#### 4.2 Python 2.x 中使用中文

> *Python 2.x 默认使用`ASCII`编码*
> *Python 3.x 默认使用`Unicode`编码*

* 在Python 2.x文件的**第一行** 增加如下代码，解释器会以`UTF-8`编码来处理`python`文件

```python
# *-* coding:utf8 *-*
```

> ***这是官方推荐使用的方式***

* 也可以使用

```python
# coding=utf8
```

## Lesson 392 文本编码3

**unicode 字符串**

* 在`Python 2.x`中，即使指定了文件使用`UTF-8`的编码格式，但是在遍历字符串时，仍然会 **以字节为单位遍历** 字符串
* 要能够 **正确的遍历字符串，** 在定义字符串时，需要 **在字符串的引号前，** 增加一个小写字母`u`，告诉解释器这是一个`unicode`字符串（使用`UTF-8`编码格式的字符串）

```python
# 引号前加u，表示是一个utf8字符
str1 = u"hello世界"
print(str1)
for c in str1:
    print(c)
```

## Lesson 393 eval基本使用

#### eval函数

`eval()`函数十分强大—— **将字符串** 当成 **有效的表达式** 来求值 并 **返回计算结果**

```python
# 基本的数学计算
In [1]: eval("1+1")
Out[1]: 2
  
# 字符串重复
In [2]: eval("'*' * 10")
Out[2]: '**********'
  
# 将字符串转换成列表
In [3]: type(eval("[1,2,3,4]"))
Out[3]: list
  
# 将字符串转换成字典
In [4]: type(eval("{'name':'xiaoming','age':18}"))
Out[4]: dict
```



**案例—计算器**

**需求**

1. 提示用户输入一个 **加减乘除混合运算**
2. 返回计算结果

```python
text = input("请输入算式：")
print(eval(text))
```

## Lesson 394 eval不要直接转换input结果

**不要滥用eval**

> ***在开发时千万不要使用`eval`直接转换`input`的结果***

```python
__import__('os').system('ls')
```

* 等价代码

```python
import os
os.system("终端命令")
```

* **执行成功，返回0**
* **执行失败，返回错误信息**



# **Part4 飞机大战项目**

## lesson 395 明确目标和实战步骤

**项目实战——飞机大战**

**目标**

* 强化 **面向对象** 程序设计
* 体验使用 `pygame`模块进行 **游戏开发**
**实战步骤**
1. `pygame`快速体验
2. **飞机大战** 实战

**确认模块 —— pygame**

* `pygame`就是一个Python模块，专为电子游戏设计
* 官方网站 https://www.pygame.org
  * **提示：** 要学习第三方模块，通常最好的参考资料就在官方网站
|网站栏目|内容|
|:----|:----|
|GettingStarted|在各平台安装模块的说明|
|Docs|pygame模块所有 **类** 和 **子类** 的参考手册|


## lesson 396 pygame模块正确安装
## lesson 397 游戏快速体验
## lesson 398 游戏初始化和退出
## lesson 399 
## lesson 400
## lesson 401
## lesson 402
## lesson 403
## lesson 404
## lesson 405
## lesson 406
## lesson 407
## lesson 408
## lesson 409
## lesson 410
## lesson 411
## lesson 412
## lesson 413
## lesson 414
## lesson 415
## lesson 416
## lesson 417
## lesson 418
## lesson 419
## lesson 420
## lesson 421
## lesson 422
## lesson 423
## lesson 424
## lesson 425
## lesson 426
## lesson 427
## lesson 428
## lesson 429
## lesson 430
## lesson 431
## lesson 432
## lesson 433
## lesson 434
## lesson 435
## lesson 436
## lesson 437
## lesson 438
## lesson 439
## lesson 440
## lesson 441
## lesson 442

# **Part5 Python高级**
## lesson 443 网络通信概述
## lesson 444 IP地址
## lesson 445 Linux、windows查看网卡
## lesson 446 ipv4和ipv6介绍
## lesson 447 端口（重点）
## lesson 448 端口分类
## lesson 449 socket介绍
## lesson 450 udp1
## lesson 451 udp2
## lesson 452 udp3
## lesson 453 udp4
## lesson 454 udp5
## lesson 455 udp6
## lesson 456 udp7
## lesson 457 udp8
## lesson 458 udp9
## lesson 459 udp10
## lesson 460 tcp介绍
## lesson 461 tcp客户端
## lesson 462 tcp服务器1
## lesson 463
## lesson 464
## lesson 465
## lesson 466
## lesson 467
## lesson 468
## lesson 469
## lesson 470
## lesson 471
## lesson 472
## lesson 473
## lesson 474
## lesson 475
## lesson 476
## lesson 477
## lesson 478
## lesson 479
## lesson 480
## lesson 481
## lesson 482
## lesson 483
## lesson 484
## lesson 485
## lesson 486
## lesson 487
## lesson 488
## lesson 489
## lesson 490
## lesson 491
## lesson 492
## lesson 493
## lesson 494
## lesson 495
## lesson 496
## lesson 497
## lesson 498
## lesson 499
## lesson 500
## lesson 501
## lesson 502
## lesson 503
## lesson 504
## lesson 505
## lesson 506
## lesson 507
## lesson 508
## lesson 509
## lesson 510
## lesson 511
## lesson 512
## lesson 513
## lesson 514
## lesson 515
## lesson 516
## lesson 517
## lesson 518
## lesson 519
## lesson 520
## lesson 521
## lesson 522
## lesson 523
## lesson 524
## lesson 525
## lesson 526
## lesson 527
## lesson 528
## lesson 529
## lesson 530
## lesson 531
## lesson 532
## lesson 533
## lesson 534
## lesson 535
## lesson 536
## lesson 537
## lesson 538
## lesson 539
## lesson 540
## lesson 541
## lesson 542
## lesson 543
## lesson 544
## lesson 545
## lesson 546
## lesson 547
## lesson 548
## lesson 549
## lesson 550
## lesson 551
## lesson 552
## lesson 553
## lesson 554
## lesson 555
## lesson 556
## lesson 557
## lesson 558
## lesson 559
## lesson 560
## lesson 561
## lesson 562
## lesson 563
## lesson 564
## lesson 565
## lesson 566
## lesson 567
## lesson 568
## lesson 569
## lesson 570
## lesson 571
## lesson 572
## lesson 573
## lesson 574
## lesson 575
## lesson 576
## lesson 577
## lesson 578
## lesson 579
## lesson 580
## lesson 581
## lesson 582
## lesson 583
## lesson 584
## lesson 585
## lesson 586
## lesson 587
## lesson 588
## lesson 589
## lesson 590
## lesson 591
## lesson 592
## lesson 593
## lesson 594
## lesson 595
## lesson 596
## lesson 597
## lesson 598
## lesson 599
## lesson 600
## lesson 601
## lesson 602
## lesson 603
## lesson 604
## lesson 605
## lesson 606
## lesson 607
## lesson 608
## lesson 609
## lesson 610
## lesson 611
## lesson 612
## lesson 613
## lesson 614
## lesson 615
## lesson 616
## lesson 617
## lesson 618
## lesson 619
## lesson 620
## lesson 621
## lesson 622
## lesson 623
## lesson 624
## lesson 625
## lesson 626
## lesson 627
## lesson 628
## lesson 629
## lesson 630
## lesson 631
## lesson 632
## lesson 633
## lesson 634
## lesson 635
## lesson 636
## lesson 637
## lesson 638
## lesson 639
## lesson 640
## lesson 641
## lesson 642
## lesson 643
## lesson 644
## lesson 645
## lesson 646
## lesson 647
## lesson 648
## lesson 649
## lesson 650
## lesson 651
## lesson 652
## lesson 653
## lesson 654
## lesson 655
## lesson 656
## lesson 657
## lesson 658
## lesson 659
## lesson 660
## lesson 661
## lesson 662
## lesson 663
## lesson 664
## lesson 665
## lesson 666
## lesson 667
## lesson 668
## lesson 669
## lesson 670
## lesson 671
## lesson 672
## lesson 673
## lesson 674
## lesson 675
## lesson 676
## lesson 677
## lesson 678
## lesson 679
## lesson 680
## lesson 681
## lesson 682
## lesson 683
## lesson 684
## lesson 685
## lesson 686
## lesson 687
## lesson 688
## lesson 689
## lesson 690
## lesson 691
## lesson 692
## lesson 693
## lesson 694
## lesson 695
## lesson 696
## lesson 697
## lesson 698













