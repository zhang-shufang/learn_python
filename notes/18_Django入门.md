[TOC]

# 18 Django入门

Django是目前最流行的Python Web框架，能够创建同时作为动态网站和移动应用程序的项目。

## 18.1 建立项目

### 制定规范

 在着手开发像web这样的大型项目时，首先需要指定规范（spec），对项目目标进行描述。确定要达成的目标后，就能着手找出为达成这些目标而需要完成的任务了。可以参考的规范如下：

```
我们需要编写一个名为“学习笔记”的Web应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条目。“学习笔记”的主页对这个网站进行描述，并邀请用户注册或登录。用户登录后，可以创建新主题、添加新条目以及阅读既有条目。
```

> 以上并没有制定完整的项目规划，只列出一些明确的目标，以突出开发的重点。

### 建立虚拟环境

#### **创建虚拟环境**

通过终端进入目标目录`target_dir`，在目标目录下执行如下命令，以创建虚拟环境：

```
target_dir$ python -m venv env_name
```

这里使用python命令运行模块`venv`，并创建了一个名为`env_name`的虚拟环境，

> 模块名为虚拟环境（virtual environment）的缩写。

#### **激活虚拟环境**

在目标目录下执行如下命令，可激活虚拟环境：

```
target_dir$ source env_name/bin/activate
(env_name)target_dir$
```

激活后的虚拟环境会在目录名前面显示`(env_name)`

要停止使用虚拟环境，可以使用如下命令：

```
(env_name)target_dir$ deactivate
target_dir$
```

#### **安装Django**

激活虚拟环境后，使用如下命令来更新pip并安装Django：

```
(env_name)target_dir$ pip install --upgrade pip
(env_name)target_dir$ pip install django
```

> 注1：由于pip从各种地方下载资源，因此升级频繁，所以每当你搭建好新环境后，都最好更新pip。
>
> 注2：由于在虚拟环境中工作，因此不管使用什么系统，安装Django的命令都相同，不需要指定`--user`，也无须使用像 `python -m pip install package_name`这样较长的命令。
>
> 注3：Django仅在虚拟环境激活是才可用。

#### **在Django中创建项目**

在虚拟环境中，执行如下命令新建一个项目：

```
(env_name)target_dir$ django-admin startproject project_name .
(env_name)target_dir$ ls
env_name project_name manage.py
(env_name)target_dir$ ls project_name
__init__.py asgi.py settings.py urls.py wsgi.py
```

命令`startproject`让Django新建一个名为project_name的项目。这个命令**末尾的句点（.）**让新项目使用适合的目录结构，这样在开发完成后可轻松地将应用程序部署到服务器上。

> 忘记句点可能会导致在部署应用程序时将遭遇一些配置问题。如果忘记了，需要删除已创建的文件和文件夹（env_name除外）， 再重新运行这个命令。
>
> PS：目前测试结果是，没有句点会导致 manage.py 文件消失。

#### **创建/更新数据库**

在虚拟环境激活的情况下，使用下面的命令可以创建数据库：

```
(env_name)target_dir$ python manage.py migrate
--snip--
(env_name)target_dir$ ls
db.sqlite3 env_name project_name manage.py
```

创建数据库所使用的命令为**迁移（migrate）**数据库，**首次执行将让 Django 确保数据库与项目的当前状态匹配**。此处通过 ls 命令可以看到 Django 创建了一个名为 db.sqlite3的文件，其是基于 SQLite 而创建的。SQLite 是一种使用单个文件的数据库，能够让开发者不用太关注数据库的管理，在编写简单应用程序时很有帮助。

#### **运行并查看**

通过以下命令，来运行 Django 服务：

```
(env_name)target_dir$ python manage.py runserver
--snip--

System check identified no issues (0 silenced)							注1
--snip--
Django version 4.1, using settings 'project_name.settings'	注2
Starting development server at http://127.0.0.1:8000/				注3
Quit the server with CONTROL-C
```

> 注1：Django 通过检查确认正确地创建了项目。
>
> 注2：Django 版本以及当前使用的设置文件的名称。
>
> 注3：项目的URL，其表明项目想在你的计算机（即 localhost）的端口8000上侦听请求。

最后在浏览器中输入URL，若看到有 “The install worked successfully!" 的字样，即表明目前一切正常。

## 18.2 创建应用程序

### 创建应用程序框架

在 runserver 运行的情况下，打开另一个终端窗口，切换到 manage.py所在的目录，激活虚拟环境后执行命令 `startapp`：

```
(venv_name)project_name$ python manage.py startapp apps_name
```

命令运行后，会产生一个 apps_name 文件夹，文件夹内最重要的文件是 models.py、 admin.py、 views.py。我们将使用 models.py 来定义要在应用程序中管理的数据。

### 定义模型

打开文件 `models.py` ，可以在里面增加网站所需要的数据模型（即对现实世界的抽象），例如书中所描述的：

```py
from django.db import models

# create your models in here

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """返回模型的字符串表示"""
        return self.text
```

> 具体函数的使用不在此说明，可参照官方文档：https://docs.djangoproject.com/en/4.2/ref/models/fields/

### 添加应用程序到 settings.py

需要将应用程序添加到 Django 的安装目录中。

打开 `settings.py` （文件位于其他文件夹中）将需要添加的应用程序添加到 `INSTALLED_APPS` 中：

```py
--snip--
INSTALLED_APPS = [
  # My apps
  'apps_folder_name',					# 注意 “,”，否则会报错
  
  # apps that django added by default
  'django.contrib.admin',
  --snip--
]
```

注意：需要将自己的应用程序放在默认的应用程序前面，这样才能覆盖默认程序的行为。

### 进行数据库迁移

#### 制作数据库迁移文件

运行以下命令，Django将会自动检查models.py文件中的模型变化，并为每个模型生成一个新的迁移文件：

```
(venv_name)project_name$ python manage.py makemigrations apps_name
Migrations for 'apps_folder_name':
  	learning_logs/migrations/0001_initial.py
    	- Create model Topic
```

#### 应用迁移文件

运行以下命令，Django将会自动应用这些迁移，更新数据库中的表结构以匹配你的模型：

```
(venv_name)project_name$ python3 manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, apps_folder_name, sessions
Running migrations:
 	Applying learning_logs.0001_initial... ok

```

### 管理站

Django 提供的 **管理站(admin site)**，能够让非普通用户轻松地处理模型。其主要使用方法为：

#### 创建超级用户

执行以下命令以创建超级用户：

```
(venv_name)project_name$ python3 manage.py createsuperuser
```

输入命令后按照提示输入管理员信息后，即可完成创建。

#### 向网站注册模型

Django 会自动在管理站中注册一些模型，例如 User 和 Group，如果要添加自定义的模型，则必须手动创建。

创建方法为：

1. 在 `models.py` 所在的目录下，找到 `admin.py` 文件（创建应用程序时，Django自动为我们创建）。

2. 在 `admin.py` 文件中手动注册添加的模型：

   ```python
   from django.contrib import admin	# django自带
   
   from .models import Model_name
   
   admin.site.register(Model_name)
   ```

   首先导入模型，modles前面的句点让 Django 在 admin.py 所在的目录中查找 models.py。

   导入完成后，通过  `admin.site.register()` 注册对应的模型。

### 后续添加新的模型

后续添加新的模型主要遵循以下几步：

1. 在 models.py 中定义新的模型。

   ```python
   class Entry(models.Model):
     """学到的有关某个主题的具体知识"""
     topic = models.ForeignKey(Topic, on_delet=models.CASCADE)
     text = models.TextField()
     date_added = models.DateTimeField(auto_now_add=True)
     
     class Meta:
       verbose_name_plural = 'entries'
       
     def __str__(self):
       """返回一个表示条目的简单字符串"""
       return f"{self.text[:50]}"
   ```

   上述代码中：

   **外键（foreign key）**是一个数据库术语，它指向数据库中的另一条记录，这里则是将每个条目关联到特定的主题。

   **实参 on_delet**=models.CASCADE 让 Django 在删除主题的同时删除所有与之相关联的条目，这杯成为级联删除（cascading delete）。

   **TextField**的实例，其长度不受限制。

   嵌套的 **Meta 类**，储存用于管理模型的额外信息。这里，它让我们能够设置一个特殊属性，让 Django 在需要时使用 Entries 表示多个条目。如果没有这个类，Django 将使用错误的复数 Entrys 来表示多个条目。

   

2. 对新定义的模型进行数据库迁移。

3. 向管理站注册新的模型。

### Django shell

Django shell 是一种通过交互式终端会话，以编程的方式查看数据的交互式环境。常用于测试项目和排除故障。以下为示例：

```
(ll_env)learning_log$ python3 manage.py shell
>>> from learning_logs.models import Topic
>>> Topic.objects.all()
<QuerySet [<Topic: Chess>, <Topic: RockClimbing>]>
```

要通过外键关系获取数据，可使用相关模型的小写名称、下划线和单词set：

```
>>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry: In the opening phase of the game, it's important t...>]>
```

假设有模型 Pizza 和 Topping，而 Topping 通过一个外键关联到 Pizza。如果有一个名为 my_pizza 的 Pizza 对象，就可以使用代码 my_pizza.topping_set.all() 来获取这张披萨的所有配料。

## 18.3 创建主页

Django 创建网页的过程分为三个阶段：

- 定义 URL ：URL 模式描述了 URL 的构成，让 Django 知道如何将浏览器请求与网站 URL 匹配，以确定返回哪个网页。
- 编写视图：每个 URL 都被映射到特定的视图。视图函数获取并处理网页所需的数据。视图函数通常使用模板来渲染网页。
- 编写模板：模板定义了网页的总体结构。

#### 映射URL

1. 在**项目主文件夹中**，找到 urls.py 并打开，添加如下代码：

```python
from django.urls import path, include

urlpatterns = [
  path('', include('apps_fold_name.urls')),
]
```

2. **在应用文件夹中**，新建 urls.py 并打开，添加如下代码：

```python
"""定义 apps_fold_name 的URL模式"""
from django.urls import path							# 1

from . import views 											# 2

app_name = 'apps_fold_name'								# 3
urlpatterns = [														# 4
  # 主页
  path('', views.index, name='index'),		# 5
]
```

默认的 urls.py 在项目主文件夹中，现在需要在应用文件夹中再创建一个 urls.py 文件，并导入上述代码。

1 ：开头的文档字符串用于指出该 urls.py 文件位于哪个文件夹。

2 ：导入 view 模块，其中的句点让 Python 从当前所在的文件夹导入 views。

3 ：变量 `app_name` 能够将这个 urls.py 文件与项目内其他应用程序中的同名文件区分开来。

4 ：列表变量 `urlpatterns` ，包含可在应用程序 learning_logs 中请求的网页。

5 ：实际的 URL 模式是对 `path()` 函数的调用，这个函数接受三个实参：

​	第一个实参是一个字符串，帮助 Django 正确地路由（route）请求。收到请求的 URL后，Django 力图将请求路由给一个**视图**，并为此搜索所有的 URL 模式，以找到与当前请求匹配的。Django 忽略项目的基础 URL（http://localhost:8000/)，因此空字符串（''）与基础 URL 匹配。 其他 URL 都与这个模式不匹配。如果请求的 URL 与任何既有 URL 模式都不匹配，Django 将返回一个错误页面。

​	第二个实参制定了要调用 view.py 中的哪个函数。当请求的 URL 与前述正则表达式匹配时，Django 将调用 view.py 中的 index() 函数。

​	第三个实参将这个 URL 模式的名称指定为 index，让我们能够在其他项目文件中轻松地引用它。每当需要提供这个主页的链接时，都将使用这个名称，而不编写URL。

#### 编写视图

视图函数接受请求中的信息，准备好生成网页所需的数据，再将这些数据发送给浏览器。这通常是使用定义网页外观的模版实现的。

apps_file_name 文件夹中的 views.py 是执行命令 python manage.py startup 时自动生成的，其当前内容如下：

```python
from django.shortcuts import render
```

当前文件只导入了 render() 函数，其可以根据视图提供的数据进行渲染。

在该文件中，添加以下代码可以为主页编写视图：

```python
def index(request):
  """学习笔记主页"""
  return render(request, 'apps_fold_name/index.html')
```

当 URL 请求与刚才定义的模式匹配时， Django 将在文件 views.py 中查找 index() 函数，再将对象 request 传递给这个视图函数。这里不需要处理任何数据，因此这个函数只包含调用 render() 的代码。这里向 render() 函数提供了两个实参：对象 request 和一个可用于创建网页的模板。

#### 编写模板

模板定义了网页的外观。每当网页被请求时，Django 都将填入相关的数据。模板让你能够访问视图提供的任何数据。

在 apps_fold_name 文件夹中新建一个文件夹，并将其命名为 templates。在该文件夹中，再新建一个文件夹并将其命名为 apps_fold_name。虽然这看起来有点多余，但这能够建立起 Django 能够解读的文件结构，即使项目很大、包含很多应用程序时也是如此。在最里面的文件夹 apps_fold_name 中，新建一个文件并将其命名为 index.html（其路径为 apps_fold_name/templates/apps_fole_name/index_html)，再在其中编写如下代码：

```html
<p>
  Learning Log
</p>
<p>
  Learning Log helps you keep track for your learning, for any topic you're interested in.
</p>
```

上述代码使用 HTML 来进行编写。

现在，如果请求这个项目的基础 URL http://localhost:8000/ ，将看到刚才创建的网页，而不是默认的 Django 网页。Django 接受请求的 URL，发现该 URL 与模式' '匹配，因此调用 view.index() 函数。这将使用 index.html 包含的模板来渲染网页。

将 URL、视图和模板分离的方式，能够让我们分别考虑项目的不同方面，在项目很大时，可让各个参与者专注于自己最擅长的那个方面。例如，数据库专家专注于模型，程序员专注于视图代码，而前端专家专注于模板。

> 注意：当出现如下错误时，可尝试停用并重启服务器。
>
> ​	ModuleNotFoundError: No module named 'learning_logs.urls'

#### 创建主页相关报错：

> django.template.exceptions.TemplateDoesNotExist: meal_planner_apps/index.html

没有将应用程序文件夹添加到 settings.py

> ModuleNotFoundError: No module named 'meal_planner_appsdjango'

settings.py 中的应用程序文件夹字符串后没有逗号

> django.core.exceptions.ImproperlyConfigured: 
>
> --snip--
>
> If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.

project 的 urls.py 中 include() 函数内没有加 `.urls`

## 18.4 创建其他网页

在基础的主页跑通以后，就可以开始扩充网页了。对于每个网页，我们都将指定 URL 模式并且编写一个视图函数和一个模板。

### 模板继承

在创建网页时，一些通用元素会出现在所有网页中。因此可编写一个包含通用元素的父模板，并让每个网页都继承父模板，而不是在每个网页中重复定义这些通用元素。

#### 创建父模板

在 index.html 所在的目录下创建一个 base.html 的模板，这个模板包含所有页面都有的元素，而其他模板都继承它。以下为父模板代码：

```html
<p>
  <a href="{% url 'apps_fold_name:index' %}">Learning Log</a>		# 1
</p>

{% block content%}{% endblock content %}																# 2
```

**模板标签**：其实质是一小段代码，使用花括号和百分号表示（{% %}）。

1：包含项目名的段落，该段落也是主页的链接。该部分使用了模板标签 {% url 'apps_fold_name:index' %} 生成一个 URL，该 URL 与 apps_fold_name/urls.py 中定义的名为 index 的 URL 模式匹配。在这个示例中，apps_fold_name 是一个**命名空间**，而 index 是该命名空间中一个名称独特的 URL 模式。这个命名空间来自在文件 apps_fold_name/urls.py 中赋给 app_name 的值。

通过模板标签来生成 URL，能很容易地确保链接是最新的：只需要修改 urls.py 中的 URL 模式，Django 就会在网页被请求时自动插入修改后的 URL。

2：在此处插入了一对**块标签**，块名为 content，是一个占位符，其中包含的信息由子模板指定。子模板并非必须定义父模板中的每个块，因此在父模板中，可以使用任意多个块来预留空间，而子模板可根据需要定义相应数量的块。

#### 创建子模板

重写 index.html，使其继承 base.html：

```html
{% extends 'apps_fold_name/base.html' %}		# 1

{% block content %}			# 2
	<p>
  	Learning Log helps you keep track of your learning, for any topic you're interested in.  
	</p>
{% endblock content %}	# 3
```

与原代码想比较，发现标题被指定要继承哪个模板的代码取代了（见 1）

子模板的第一行必须包含标签 {% extends %}，让 Django 知道它继承了哪个父模板。这行代码导入模板 base.html 的所有内容，让 index.html 能够指定要在 content 块预留的空间中添加的内容。

我们插入一个名为 content 的{% block %}标签，以定义 content 块（见2）。使用标签 {% end block content %} 指出内容定义的结束位置（见3）。在标签 {% end block %} 中，并非必须指定块名，但如果模块包含多个块，指定块名有助于确定结束的是哪个块。

模板继承的优点：在子模板中，只需包含当前网页特有的内容。这不仅简化了每个模板，还使得网站修改起来容易得多。要修改多个网页共同包含的元素，只需要修改父模板即可，所做的修改将传导到继承该父模板的每个页面。在网页数量较多的情况下，这种模式对于维护和更新网站都大有裨益。

在大型项目中，通常有一个用于整个网站的父模板 base.html，且网站的每个主要部分都有一个父模板。网站的各部分父模板继承 base.html，网站的具体网页则继承对应部分的父模板。

### 显示所有主题的页面

所有主题页面显示用户创建的所有主题，它是第一个需要使用数据的网页。

#### URL模式

首先定义显示所有主题的页面的 URL，通常，使用一个简单的 URL 片段来指出网页显示的信息；这里使用单词 topics。因此 URL http://localhost:8000/topics/ 将返回显示所有主题的页面。下面演示该如何修改 learning_logs/urls.py：

```python
"""为 learning_logs 定义 URL 模式"""
--snip--
urlpatterns = [
  # 主页
  path('', views.index, name='index'),
  # 显示所有主题的页面
  path('topics/', views.topics, name='topics')
]
```

新的 URL 模式为 topics/。在 Django 检查请求的 URL 时，这个模式将与如下 URL 匹配：基础 URL 后面跟着 topics。URL 与该模式匹配的请求都将交给 views.py 中的 topics() 函数。

#### 视图

topics() 函数需要从数据库中获取一些数据，并将其交给模板。因此需要在 views.py 中添加如下代码：

```python
from .models import Topic		# 1

--snip--

def topics(request):				# 2 
  """显示所有主题"""
  topics = Topic.objects.order_by('date_added')										# 3
  context = {'topics': topics}																		# 4
  return render(request, 'learning_logs/topics.html', context)		# 5

```

1：导入与所需数据相关联的模型。

2：函数 topics() 包含一个形参：即 Django 从服务器哪里收到的 request 对象。

3：我们查询数据库：请求提供 Topic 对象，并根据属性 date_added 进行排序，并赋值给 topics。

4：定义一个将发送个模板的 `context`，其格式为字典，其中的键是用来在模板中访问数据的名称，而值是要发送给模板的数据。

5：在创建使用数据的网页时，调用了 `render()`，并向它传递对象 `request`、要使用的模板和字典 `context`。

#### 模板

显示所有主题的页面的模板接受字典 context，以便能够使用 topics() 提供的数据。新建一个文件，将其命名为 topics.html，并储存到 index.html 所在的目录中：

```html
{% extends 'learning_logs/base.html' %}

{% block content %}
	
  <p>Topics</p>
  
	<ul>																						# 1
    {% for topic in topics %}											# 2
    	<li>{{ topic.text }}</li>										# 3
    {% empty %}																		# 4
    	<li>No topics have been added yet.</li>
    {% endfor %}																	# 5
	</ul>																						# 6

{% endblock content %}
```

开头同样使用 {% extends %} 来继承 base.html，然后在定义 content 块。这个网页的主体是一个项目列表，其中列出了用户输入的主题。

1：在标准 HTML 中，项目列表称为**无序列表**，用标签 <ul></ul> 表示。包含所有主题的项目列表始于起始标签 <ul> 。

2：使用一个相当于 for 循环的模板标签，它遍历字典 context 中的列表 topics。

> 注：模板中使用的代码与 Python 代码存在一些重要差别： Python 使用缩进来指出哪些代码是 for 循环的组成部份；而在模板中，每个 for 循环都必须使用 {% endfor %} 标签来显示地指出结束位置。因此在模板中，循环类似于下面这样：

```html
{% for item in list %}
	do something with each time
{% endfor %}
```

3：要在模板中打印变量，需要将变量名用双花括号括起。这些花括号用于告诉 Django 我们使用了一个模板变量。因此每次循环时，代码 {{ topic.text }} 都会被替换为当前主题的 text 属性。HTML 标签 <li></li> 表示一个项目列表项。在标签对 <li></li> 内部，位于标签之间的内容都是一个项目列表项。

4: 模板标签 {% empty %} 告诉 Django 在列表 topics 为空时该怎么办。

5: 结束 for 循环。

6: 结束项目列表。

**调整父模板，以使其包含显示所有主题的页面的链接。**

在 base.html 中添加如下代码：

```html
<p>
  <a href="{% url 'apps_fold_name:index' %}">Learning Log</a>	-	# 1
  <a href="{% url 'apps_fold_name:topics' %}">Topics</a>
</p>

{% block content%}{% end block %}																# 2
```

1: 添加一个连字符 `-`。

2: 使用模板标签 {% url %} 再添加一个显示所有主题的页面的链接，这能够让 Django 生成一个与 learning_logs/urls.py 中名为 topics 的 URL 模式匹配的链接。



### 显示特定主题的页面

创建一个专注于特定主题的页面，用于显示该主题的名称及其所有条目。

#### URL 模式

显示特定主题页面的 URL 模式与前面的所有 URL 模式都稍有不同，因为它使用主题的 id 属性来指出请求的是哪个主题。如果用户要查看主题 Chess （其 id 为1）的详细页面，URL 将为 http://localhost:8000/topics/1/。下面是与这个 URL 匹配的模式，它应该放在 learning_logs/urls.py 中：

```python
--snip--
urlpatterns = [
  --snip--
  # 特定主题的详细页面
  path('topics/<int:topic_id>/', views.topic, name='topic'),
]
```

这个 URL 模式中的字符串 `'topic/<int:topic_id>/'`，第一部分（topics）让 Django 查找在基础 URL 后紧跟单词 topics 的 URL，第二部分（`/<int:topic_id>/`）与在两个斜杠之间的整数匹配，并将这个整数赋值给实参 topic_id。当发现 URL 与这个模式匹配的时候，Django 将调用视图函数 topic()，并将 topic_id 的值作为实参传递给它。在这个函数中，将使用 topic_id 的值来获取相应的主题。

#### 视图

topic() 函数需要从数据库中获取指定的主题以及与之相关联的所有条目（就像前面在 Django shell 中所做的一样）：

```python
--snip--
def topic(request, topic_id):																			# 1
	"""显示单个主题及其所有的条目"""		
  topic = Topic.objects.get(id=topic_id)													# 2
  entries = topic.entry_set.order_by('-date_added')								# 3
  context = {'topic': topic, 'entries': entries}									# 4
  return render(request, 'learning_logs/topic.html', context)			# 5
```

1: 这是第一个除了 request 对象外，还包含另一个形参的视图函数。这个函数接受表达式 `/<int:topic_id>/` 捕获的值，并将其赋值给 topic_id 。

2: 使用 get() 来获得指定的主题，此处与 Django shell 所做的一样。

3: 获取与该主题想关联的条目，并根据 date_added 进行排序。其前面的符号将指定按降序排序。

4: 将主题和条目都储存到字典 context 中。

5: 调用 render() 并向它传递 request 对象、模板 topic.html 和字典 context。

> 2和3处的代码称为**查询**，因为它们向数据库中查询特定的信息。如果要在自己的项目中编写这样的查询，现在 Django shell 中进行尝试大有裨益。比起先编写视图和模板，再在浏览器中检查结果，在 shell 中执行代码可更快获得反馈。

#### 模板

这个模板需要显示主题的名称和条目的内容。如果当前主题不包含任何条目，还需要向用户指出这一点，模板名称为 topic.html，代码如下：

```html
{% extends 'learning_logs/base.html' %}

{% block content %}
	<p>Topic: {{ topic.text }}</p>															# 1

	<p>Entries:</p>
	<ul>																												# 2
    {% for entry in entries %}																# 3
    	<li>
    		<p>{{ entry.date_added|date:'M d, Y H:i' }}</p>				# 4
        <p>{{ entry.text|linebreaks }}</p>										# 5
    	</li>
    {% empty %}																								# 6
    	<li>There are no entries for this topic yet.</li>
    {% endfor %}
	</ul>

{% endblock content %}
```

1: 显示请求的主题的 text 属性。变量 topic 已经由字典 context 传入。

2: 显示每个条目的项目列表。

3: 像前面显示所有主题一样遍历条目。

4 & 5: 每个项目列表都将列出两条信息：条目的时间戳和完整的文本。列出时间戳需要显示属性 date_added 的值，列出内容需要显示属性 text 的值。

> 注：在 Django 模板中，竖线 `|` 表示模板**过滤器**：即在渲染过程中对模板变量的值进行修改的函数。过滤器 date: 'M d, Y H : i ' 以类似下面这样的格式显示时间戳：January 1, 2022 23:00。过滤器 linebreaks 将包含换行符的长条目转换为浏览器能够理解的格式，以免显示为不间断的文本块。

6: 显示在没有条目的情况下的内容。

#### 链接补全

将显示所有主题的页面中的每个主题都设置为链接，即需要修改 topics.html，让每个主题都能链接到相应的网页，如下所示：

```html
--snip--
	{% for topic in topics %}
		<li>
			<a href="{% url 'learning_logs:topic' topic.id %}">
      	{{ topic.text }}</a>
		</li>
```

我们使用模板标签 url 根据 learning_logs 中名为 topic 的 URL 模式生成了合适的链接。这个 URL 模式要求提供实参 topic_id，因此在模板标签 url 中添加了属性 topic.id。现在，主题列表中的每个主题都是链接了，并且链接到显示相应主题的页面，如 http://localhost:8000/topics/1/。

## 18.5 总结

基本的路径是：

1. **urls.py**：在 urls.py 中确定 url 路径，并引出 views.py 中需要定义的函数。
2. **views.py**：根据 urls.py 中所定义的函数，提取所需要的数据，并传递出渲染文件（`return render()`）给浏览器（模板）。
3. **.html**：所谓的模板文件，描述具体的网页显示内容和格式，将 views.py 传递出的数据填入到网页的对应位置。
