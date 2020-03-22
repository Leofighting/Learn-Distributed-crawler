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
>
> 



