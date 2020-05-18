.. _helloworld:

文章结构
-------------
::

    *****************************************
    附录：reStructuredText简明教程 
    *****************************************
    .. sidebar:: sidebar Title

        .. contents:: 目录
        .. section-numbering:: 

.. sidebar:: sidebar Title

    .. contents:: 目录


文章层次结构一般由标题、章、节、小节、小小节等对象组成. 
定义各层次对象的方式是在对象名称下面添加不同的下划线. 例如'======='和'-----'.
为了方便，我们把文章称作一号对象，章称作二号对象，节为三号对象，以此类推.
各对象相应标题分别称作一号标题、二号标题、三号标题等待。

下面为各对象标题的一种常用表示方法::

    一号标题：对应整篇文章
    ===========================

    二号标题：对应章
    ----------------------------

    三号标题：对应节
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    四号标题：对应小节
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    五号标题：对应小小节
    #############################

说明:

1. '====' 这些符号至少和文字行一样长, 更长也行
#. 相同级别必须使用统一的符号, 否则会被识别为更小的级别
#. ``= - ~ ` : ' " ^ _ * _ # < >`` 这些符号都可以, 级别足够多了
#. 各级标题所用的符号必须一致，例如所有三号标题都用 ``^^^^^`` 表示

段落
--------------------
标题约定:

.. code::

    一号 ====================
    二号 --------------------
    三号 ^^^^^^^^^^^^^^^^^^^^
    四号 """""""""""""""""""""


| 段落块标记: ("|")。This is a line block.  It ends with a blank line.
|     Each new line begins with a vertical bar ("|").
|     Line breaks and initial indents are preserved.
| Continuation lines are wrapped portions of long lines;
 they begin with a space in place of the vertical bar.
|     The left edge of a continuation line need not be aligned with
  the left edge of the text above it.

| This is a second line block.
|
| Blank lines are permitted internally, but they must begin with a "|".

This is a line.

This is another line.

| This Line 1.
| And this is Line 2.

|
|   This line starts with 2 spaces.

|   但是，这一行开始并没有空格缩进。`hello`,``World!``, *hello*, **World**

Block Quotes
^^^^^^^^^^^^^^^^^^^^^
Block quotes consist of indented body elements:

    My theory by A. Elk.  Brackets Miss, brackets.  This theory goes
    as follows and begins now.  All brontosauruses are thin at one
    end, much much thicker in the middle and then thin again at the
    far end.  That is my theory, it is mine, and belongs to me and I
    own it, and what it is too.

    -- Anne Elk (Miss)

分割线
^^^^^^^^^^^^^^^^^^^^

A line above.

---------

A line below.

侧边栏
^^^^^^^^^^^^^^^^^^^^

.. sidebar:: Sidebar Title
   :subtitle: Optional Subtitle

   This is a sidebar.  It is for text outside the flow of the main
   text.

   .. rubric:: This is a rubric inside a sidebar

   Sidebars often appears beside the main text with a border and
   background color.
    
复合段落
^^^^^^^^^^^^^^^^^^^^

.. compound::

  This paragraph contains a literal block::

       Connecting... OK
       Transmitting data... OK
       Disconnecting... OK

   and thus consists of a simple paragraph, a literal block, and
   another simple paragraph.  Nonetheless it is semantically *one*
   paragraph.

This construct is called a *compound paragraph* and can be produced
with the "compound" directive.


二号标题：使用链接
--------------------

描点链接
^^^^^^^^
目的地： 

.. _my-reference-label:

需引用自身, 查看 :ref:`to my reference <my-reference-label>`.
还是说这样可以：`my-reference-label`_
eg：查看这个文件本身：:ref:`helloworld`  返回 top 


外部链接
^^^^^^^^^^^^^^^^^
`链接文本 <http://www.me115.com/>`_ 可以插入网页链接

.. _colin的博客 : http://www.me115.com

`使用链接 <http:///www.me115.com>`_ 和其它的方式 `colin的博客`_.

.. _大CC的博客: http://blog.me115.com

链接文本是网址，则不需要特别标记，分析器会发现网址和邮件 `大CC的博客`_；

内部链接
^^^^^^^^^^^^
查看 top命令(top),或者是查看sar命令(sar),

标记： 

.. _example:

使用

使用这个链接：example_

本页面链接：helloworld_

尾注
--------------------
Lorem ipsum [#f1]_ dolor sit amet ... [#f2]_

.. rubric:: Footnotes

.. [#f1] 第一条尾注的文本.
.. [#f2] 第二条尾注的文本.

也可以使用自动标号的尾注：[#]_
熟悉Git\ [#]_\ 的人几乎都知道并喜欢

.. [#] http://git-scm.com/


引用：
--------------------
这里有个引用 [#f3]_  呵呵，

.. [#f3] 参考文献    

添加图片
--------------------

普通图片添加
^^^^^^^^^^^^^^^^^^^
图片路径为源文件的相对路径；或者以根目录为开始的

.. image:: ../_static/me115_com.jpg
    :height: 200px
    :align: center
    :alt: reStructuredText, the markup syntax

A figure directive with center alignment

.. figure:: ../_static/me115_com.jpg
   :align: center
   :height: 100px
   :width: 100px

An image

插图引用
^^^^^^^^^^^^^^^^^^^^
.. _fig_0601:
.. figure:: ../_static/me115_com.jpg

   插图 6-1 神奇的木书架

引用处：

fig_0601_


内联标记(单词标记)
--------------------
| 斜体：*text*  （\* 两侧各留一个空格）
| 加粗：**text**
| 代码样式：``text`` （反引号 \`\` ）
| 文本中如果有，使用反斜杠进行转义；

Paragraphs contain text and may contain inline markup: *emphasis*,
**strong emphasis**, ``inline literals``, standalone hyperlinks
(http://www.python.org), external hyperlinks (Python_), internal
cross-references (example_), external hyperlinks with embedded URIs
(`Python web site <http://www.python.org>`_), footnote references
(manually numbered [1]_, anonymous auto-numbered [#]_, labeled
auto-numbered [#label]_, or symbolic [*]_), citation references
([CIT2002]_), substitution references ``(|example|)``, and ``inline
hyperlink targets`` (see ``Targets_`` below for a reference back to here).
Character-level inline markup is also possible (although exceedingly
ugly!) in *re*\ ``Structured``\ *Text*.  Problems are indicated by
``|problematic|`` text (generated by processing errors; this one is
intentional).

The default role for interpreted text is `Title Reference`.  Here are
some explicit interpreted text roles: a PEP reference (:PEP:`287`); an
RFC reference (:RFC:`2822`) and (:RFC:`2011`); a :sub:`subscript`; a :sup:`superscript`;
and explicit roles for :emphasis:`standard` :strong:`inline`
:literal:`markup`.

.. _Python: https://python.org
.. [1] manually numbered footnote
.. [#] autonumbered footnote
.. [#label] autonumbered footnote
.. [*] autonumbered footnote
.. [#] autonumbered footnote


列表：
--------------------
仅在段落的开头放置一个星号和一个空格. 编号的列表也可以使用符号 # 自动加序号:

* 这是一个项目列表
* 有两项

用-是markdown的做法,rst同样可用：

- hello，第一列
- 第二列
- 第三列


1. 这是个有序列表
#. 还是个有序列表，自动编号

  - 列表
  - 列表

    - 嵌套列表
    - 嵌套列表

5. 继续有序列表，但序号重新指定
#. 继续前面列表序号

注：列表可以嵌套，但是使用空行分割

i) 行一
#) 行二

(I) 大写罗马字
(#) 行二

A. 大写字母
#. 行二

-a              command-line option "a"
-b file         options can have arguments
                and long descriptions
--long          options can be long also
--input=file    long options can also have
                arguments
/V              DOS/VMS-style options too

名称解释列表：
^^^^^^^^^^^^^^^^^^^^
*大CC*
    大CC的博客在这里

Definition Lists
----------------

Term
    Definition
Term : classifier
    Definition paragraph 1.

    Definition paragraph 2.

ABC : def
    definition here.
    and here. this line is the continue of the last line.

    continue here.

Another way
    definiton here

Bullet Lists
------------

- A bullet list

  + Nested bullet list.
  + Nested item 2.

- Item 2.

  Paragraph 2 of item 2.

  * Nested bullet list.
  * Nested item 2.

    - Third level.
    - Item 2.

  * Nested item 3.


特殊段落标记
--------------------

.. note::   
    
    这里是Note提示段落；

其它类似语法的还有：

* warning 一般显示的是信息安全方面的注意事项
* seealso 许多章节包含模块文档或者扩展文档的参考索引列表.这些列表由指令 seealso 创建
* centered 创建居中加粗文本行
* hlist 生成水平列表. 它将列表项横向显示并减少项目的间距使其较为紧凑


水平列表,它将列表项横向显示并减少项目的间距使其较为紧凑

.. hlist::  
   :columns: 3

   * 第一列，生成水平列表. 
   * 第二列
   * di san lie

.. hlist::
   :columns: 3

   * A list of
   * short items
   * that should be
   * displayed
   * horizontally

提示框
^^^^^^^^^^^^^^

.. Attention:: Directives at large.

.. Caution::

   Don't take any wooden nickels.

.. DANGER:: Mad scientist at work!

.. Error:: Does not compute.

.. Hint:: It's bigger than a bread box.

.. Important::
   - Wash behind your ears.
   - Clean up your room.
   - Call your mother.
   - Back up your data.

.. Note:: This is a note.

.. Tip:: 15% if the service is good.

.. WARNING:: Strong prose may provoke extreme mental exertion.
   Reader discretion is strongly advised.

.. admonition:: And, by the way...

   You can make up your own admonition too.

.. seealso::

    本书并非一本介绍Git的书，并且假设读者已经掌握了Git的相关操作。如果读者对\
    Git尚不了解，可以参考我写的 《Git权威指南》\ [#]_\ 一书。此外还可以从网上\
    找到很多免费的、很好的Git资料，如：Git社区书\ [#]_\ 、Pro Git\ [#]_\ 等。

.. 这是一个评论.

可以通过多行缩进产生多行评论：

..
   这整个缩进块都是
   一个评论.

   仍是一个评论.


嵌入程序代码
--------------------

嵌入程序代码
^^^^^^^^^^^^^
在嵌入程序代码处, 需添加两个英文冒号'::'，代码需隔一行放置，代码的左侧必须缩进, 
代码引用到没有缩进的行为止. 例如:：

    如果数据库有问题, 执行下面的 SQL\:\:

        # Dumping data for table `item_table`

        INSERT INTO item_table VALUES (
        0000000001, 0, 'Manual', '', '0.18.0',
        'This is the manual for Mantis version 0.18.0.\r\n\r\nThe Mantis manual is modeled after the [url=http://www.php.net/manual/en/]PHP Manual[/url]. It is authored via the \\"manual\\" module in Mantis CVS.  You can always view/download the latest version of this manual from [url=http://mantisbt.sourceforge.net/manual/]here[/url].',
        '', 1, 1, 20030811192655);

代码效果为：

如果数据库有问题, 执行下面的 SQL::

    # Dumping data for table `item_table`

    INSERT INTO item_table VALUES (
    0000000001, 0, 'Manual', '', '0.18.0',
    'This is the manual for Mantis version 0.18.0.\r\n\r\nThe Mantis manual is modeled after the [url=http://www.php.net/manual/en/]PHP Manual[/url]. It is authored via the \\"manual\\" module in Mantis CVS.  You can always view/download the latest version of this manual from [url=http://mantisbt.sourceforge.net/manual/]here[/url].',
    '', 1, 1, 20030811192655);

说明：

- 如果作为独立段落存在,则整段都不会出现在文档里.
- 如果前面有空白，则标记被移除.
- 如果前面是非空白，则标记被一个冒号取代.

::

    for(int i = 0;i< 10 ;i++)
    {
        cout << "hello world" << endl;
    }

高亮语法标记
^^^^^^^^^^^^^
可以 用 .. code-block:: 追加各种语法高亮声明:

.. code-block:: python   
    :linenos:   
    :emphasize-lines: 1,3

    def foo():
        print "Love Python, Love FreeDome"
        print "E文标点,.0123456789,中文标点,. "


.. code-block:: sh
    
    /opt/app/todeav1$ps -fe| grep ls
    root      3676     1  0  2012 ?        02:58:14 /usr/sbin/vmtoolsd

程序引用
^^^^^^^^^^^^^^^
外部包含:

.. literalinclude:: ../example.py
    :language: python



.. [#] http://git-scm.com/
.. [#] https://github.com/
.. [#] ISBN：9787111349679, 由机械工业出版社华章公司于2011年7月出版。
.. [#] http://book.git-scm.com/
.. [#] http://progit.org/book/
.. [#] add a reference
.. [#] another reference
.. [#] another reference again

.. _cit2003: https://cit2002.org

.. [CIT2002] Held on Florida, 1999

替换文本
--------------------

I recommend you try |Python|_.

.. |Python| replace:: Python, *the* best language around


.. topic:: Topic Title

   This is a topic.

.. rubric:: This is a rubric


表格
---------------------

.. bibliographic fields (which also require a transform):

:Author: David Goodger
:Address: 123 Example Street
          Example, EX  Canada
          A1B 2C3
:Contact: docutils-develop@lists.sourceforge.net
:Authors: Me; Myself; I
:Dedication:

    For Docutils users & co-developers.
:abstract:

    This document is a demonstration of the reStructuredText markup
    language, containing examples of all basic reStructuredText
    constructs and many advanced constructs.


列表表格
^^^^^^^^^
.. list-table:: Frozen Delights!
  :widths: 15 10 30
  :header-rows: 1

  * - Treat
    - Quantity
    - Description
  * - Albatross中文
    - 2.99
    - On a stick!
  * - Crunchy Frog
    - 1.49
    - If we took the bones out, it wouldn't be
      crunchy, now would it?
  * - Gannet Ripple
    - 1.99
    - On a stick!

CSV 表格
^^^^^^^^^
.. csv-table:: Frozen Delights!
 :header: "Treat", "Quantity", "Description"
 :widths: 15, 10, 30

 "Albatross", 2.99, "On a stick!"
 "Crunchy Frog", 1.49, "If we took the bones out, it wouldn't be
 crunchy, now would it?"
 "Gannet Ripple", 1.99, "On a stick!"

简单表格
^^^^^^^^^^
注意: 表格包含中文时,基本无法对齐.

::

    =====  =====  ======
    Inputs     Output
    ------------  ------
    A      B    A or B
    =====  =====  ======
    False  False  False
    True   False  True
    False  True   True
    True   True   True
    =====  =====  ======

生成的表格：

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

普通表格
^^^^^^^^^^
::

    +------------+------------+-----------+
    | Header 1   | Header 2   | Header 3  |
    +============+============+===========+
    | body row 1 | column 2   | column 3  |
    +------------+------------+-----------+
    | body row 2 | Cells may span columns.|
    +------------+------------+-----------+
    | body row 3 | Cells may  | - Cells   |
    +------------+ span rows. | - contain |
    | body row 4 |            | - blocks. |
    +------------+------------+-----------+

生成的表格：

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Extensions
-----------------

::

    .. plot::

        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(-6, 6, 1000)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("sin(x)")

        # 最后必须要调用 show 方法, 才能显示
        plt.show()
