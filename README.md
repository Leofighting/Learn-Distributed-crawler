## 爬虫相关基础知识

> 技术选型：`scrapy / requests + beautifulsoup`
>
> `requests  beautifulsoup`：属于库
>
> `scrapy`：是一个框架；基于 `twisted`； 可以加入 `requests  beautifulsoup`；提供了很多内置功能；内置了`css` 与 `xpath selector`

> 网页分类
>
> - 静态网页
> - 动态网页
> - `webservice(restapi)`

> 爬虫的作用
>
> 1. 搜索引擎：百度、谷歌等
> 2. 推荐引擎：今日头条
> 3. 机器学习的数据样本
> 4. 数据分析、舆情分析等

### 正则表达式

> ^：匹配输入字符串的开始位置，除非在方括号表达式中使用，当该符号在方括号表达式中使用时，表示不接受该方括号表达式中的字符集合。要匹配 ^ 字符本身，请使用 \^
>
> $：匹配输入字符串的结尾位置。如果设置了 `RegExp` 对象的 `Multiline` 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。
>
> . ：匹配除了换行符 *\n* 以外的任意一个字符
>
> *：匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*
>
> - 贪婪模式：.*
>
> ?：匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?
>
> - 费贪婪模式：.*?
>
> +：匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+
>
> {n}：n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o
>
> {n,m}：m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配` "fooooood"` 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格
>
> |： 指明两项之间的一个选择，分前后顺序，如果前面优先匹配，输出前面的内容。要匹配 |，请使用 \|  
>
> []：满足 [] 内的任意一个字符即可；[0-9] 表示：满足 0 到 9 中的任意一个数字即可；`[^]`：取反
>
> ( )：标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)
>
> \s：匹配一个任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。注意 Unicode 正则表达式会匹配全角空格符
>
> \S：匹配一个任何非空白字符。等价于 `[^ \f\n\r\t\v]`
>
> \w：任意一个字母或数字或下划线，相当于`[a-zA-Z0-9_]`
>
> \W：`\w`取反，相当于`[^a-zA-Z0-9_]`
>
> `[\u4E00-\u9FA5] `：匹配汉字
>
> \d：任意一个数字，相当于*[0-9]*，即*0~9* 中的任意一个
>
> \D：任意一个非数字字符，*\d*取反，相当于*[^0-9]*

### 深度优先和广度优先算法

> 深度优先：通过递归实现
>
> 广度优先：通过队列实现

### 字符串编码

> 1. 计算机智能处理数字，文本转换为数字才能处理
> 2. ASCII 编码成为美国人的标准编码，为了处理中文，中国制定了 `GB2312` 编码，用两个字节表示一个汉字，而且其他国家也发明了自己独有的字节编码，导致标准越来越多
> 3. Unicode 出现后，将所有语言统一到一套编码里
>    - Unicode 可以解决乱码问题，但是增加了一倍的存储空间
>    - 内存处理更简单
> 4. `utf-8` 编码的出现，把英文变为1个字节，汉字3个字节
>    - 节约了内存空间，但是增加了内存处理的复杂度
> 5. 改善：读取：转换为 Unicode 编码；保存：转换为 `utf-8` 编码

### 爬虫的去重策略

> 1. 将访问过的 `url` 保存到数据库中
> 2. 将访问过的 `url` 保存到 `set` 中，只需要 `o(1)` 时间复杂度就可以查询`url`
>    - 缺点：内存占用会越来越大
> 3. `url` 经过 `md5` 等方法哈希后保存到 `set` 中，能够将 `url` 压缩到同样的长度
> 4. 使用 `bitmap` 方法，将访问过的 `url` 通过 `hash` 函数映射到某一位
>    - 缺点：冲突非常高
> 5. 改进后使用 `bloomfilter`方法，多重 `hash` 函数降低冲突



## `scrapy`

```
Scrapy是适用于Python的一个快速、高层次的屏幕抓取和web抓取框架，用于抓取web站点并从页面中提取结构化的数据。Scrapy用途广泛，可以用于数据挖掘、监测和自动化测试。
```

[官网](https://scrapy.org/)

> 安装 `scrapy` 框架：`pip install scrapy`
>
> 新建 `scrapy` 项目：`scrapy startproject ArticleSpider`
>
> 目录结构：
>
> ![image-20200323181818527](E:\project\scrapy\scrapy_project\images\01.png)
>
> 创建爬虫项目：`scrapy genspider example example.com`

> ```python
> class JobboleSpider(scrapy.Spider):
>  name = 'jobbole'  # 应用名称
>  allowed_domains = ['http://blog.jobbole.com']
>  start_urls = ['http://http://blog.jobbole.com/']  # 待爬取的网站
> ```

> `scrapy` 项目调试程序
>
> ```python
> import sys
> import os
> 
> from scrapy.cmdline import execute
> 
> sys.path.append(os.path.dirname(os.path.abspath(__file__)))
> execute(["scrapy", "crawl", "jobbole"])
> ```

> `settings.py`
>
> ```python
> # Obey robots.txt rules
> ROBOTSTXT_OBEY = False
> ```

### `xpath`

>简介
>
>1. `xpath` 使用路径表达式在 `xml` 与 `html` 中进行导航
>2. 包含标准函数库
>3. 是一个 `w3c` 的标准

> 节点关系
>
> 1. 父节点
> 2. 子节点
> 3. 兄弟节点
> 4. 先辈节点
> 5. 后代节点

> 语法
>
> | **表达式**   | **说明**                                                     |
> | ------------ | ------------------------------------------------------------ |
> | article      | 选取所有article元素的所有子节点                              |
> | /article     | 选取根元素article                                            |
> | article/a    | 选取所有属于article的子元素的a元素                           |
> | //div        | 选取所有div子元素(不论出现在文档任何地方)                    |
> | article//div | 选取所有属于article元素的后代的div元素，不管它出现在article之下的任何位置 |
> | //@class     | 选取所有名为class的属性                                      |

> | **表达式**             | **说明**                                 |
> | ---------------------- | ---------------------------------------- |
> | /article/div[1]        | 选取属于article子元素的第一个div元素     |
> | /article/div[last()]   | 选取属于article子元素的最后一个div元素   |
> | /article/div[last()-1] | 选取属于article子元素的倒数第二个div元素 |
> | //div[@lang]           | 选取所有拥有lang属性的div元素            |
> | //div[@lang='eng']     | 选取所有lang属性为eng的div元素           |

> | **表达式**             | **说明**                                                     |
> | ---------------------- | ------------------------------------------------------------ |
> | /div/*                 | 选取属于div元素的所有子节点                                  |
> | //*                    | 选取所有元素                                                 |
> | //div[@*]              | 选取所有带属性的元素                                         |
> | /div/a \| //div/p      | 选取所有div元素的a和p元素                                    |
> | //span \| //ul         | 选取文档中的span和ul元素                                     |
> | article/div/p\| //span | 选取所有属于article元素的div元素的p元素 以及文档中所有的span元素 |

> 注意：在某些情况下，网页中的 HTML 代码，可能是由 `ajax` 生成，导致 `xpath` 路径不正确
>
> 尽量使用`//div[@lang='eng']` 的格式来避免以上问题

> 如果一个标签，其属性值很长，只需要获取其中一部分时，可以用 `contains` 
>
> 例如：`<div class="main_news content_btm_news">` ，其中，`class` 属性有两部分，只取其中一部分时，写法如下`//div[contains(@class, 'content_btm_news')]`

### `css` 选择器

> | **表达式**          | **说明**                               |
> | ------------------- | -------------------------------------- |
> | *                   | 选择所有节点                           |
> | #container          | 选择id为container的节点                |
> | .container          | 选取所有class包含container的节点       |
> | li  a               | 选取所有li下的所有a节点                |
> | ul  + p             | 选择ul后面的第一个p元素                |
> | div#container  > ul | 选取id为container的div的第一个ul子元素 |

> | **表达式**                   | **说明**                               |
> | ---------------------------- | -------------------------------------- |
> | ul ~ p                       | 选取与ul相邻的所有p元素                |
> | a[title]                     | 选取所有有title属性的a元素             |
> | a[href=“http://jobbole.com”] | 选取所有href属性为jobbole.com值的a元素 |
> | a[href*=”jobole”]            | 选取所有href属性包含jobbole的a元素     |
> | a[href^=“http”]              | 选取所有href属性值以http开头的a元素    |
> | a[href$=“.jpg”]              | 选取所有href属性值以.jpg结尾的a元素    |
> | input[type=radio]:checked    | 选择选中的radio的元素                  |

> | **表达式**          | **说明**                       |
> | ------------------- | ------------------------------ |
> | div:not(#container) | 选取所有id非container的div属性 |
> | li:nth-child(3)     | 选取第三个li元素               |
> | tr:nth-child(2n)    | 第偶数个tr                     |

> extract_first() 函数，如果有值，返回第一个，无值则返回 None， 不会报错

> 两种选择器都可以进行嵌套使用
>
> 