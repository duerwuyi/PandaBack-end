# account_management_apis

## views

### LoginForm

type: class

father: `django.forms.form`

description: 展示用户登录界面的表单.

fields:

+ email
+ password

#### clean_email

type: function

paramters: self

return_type: str

description: 检测用户提供的邮箱地址是否已注册. 如果是, 返回邮箱地址. 否则抛出`DoesNotExist`错误

pre-condition: `self.cleaned_data`中含有`email`键.

post-condition: 返回已经注册过的邮箱地址, 或者抛出错误.

#### clean_password

type: function

paramters: self

return_type: str

description: 检测用户提供的密码是否合法. 如果是, 返回密码, 否则抛出`ValidationError`错误.

pre-condition: `self.cleaned_data`中含有`password`键.

post-condition: 返回合法的密码, 或者抛出错误.

### register

type: function

paramters: request

return_type: JsonResponse对象

description: 验证经由POST方式传递进来的用户注册信息是否合法.

pre-condition: request对象中包含`username`, `password`, `email`, `repeated_password`键.

post-condition: 返回一个表示验证结果的JsonResponse对象.

### login

type: function

parameters: request

return_type: JsonResponse对象

description: 验证经由POST方式传递进来的用户登录信息是否合法.

pre-condition: request对象中包含`username`, `password`, `email`, `is_login`键.

post-condition: 返回一个表示验证结果的JsonResponse对象.

### index

type: function

paramters: request

return_type: JsonResponse对象

description: 如果requst使用GET方法, 返回用户的登录状态.

pre-condition: 无

post-condition: 返回提示用户登录状态的JsonResponse对象.

### logout

type: function

paramters: request

return_type: JsonResponse对象

description: 使用户登出

pre-condition: 无

post-condition: 结束request对应的会话, 返回表示登出成功的JsonResponse对象.

## models

### User

type: class

father: `django.db.models.Model`

description: 保存用户信息的类

fields:
+ username
+ password
+ email
+ learner_level
+ points
+ country
+ age
+ portrait_url

## middleware

### LoginCheckMiddleware

type: class

father: `django.utils.deprecation.MiddlewareMixin`

description: 在登录环节进行检查的中间件.

## forms

### UserForm

type: class

father: `django.forms.form`

description: 展示用户注册界面的表单

fields:

+ username
+ password
+ email
+ repeat_password

#### clean_email

type: function

paramters: self

return_type: str

description: 检测用户提供的邮箱地址是否已注册. 如果是, 返回邮箱地址. 否则抛出`DoesNotExist`错误

pre-condition: `self.cleaned_data`中含有`email`键.

post-condition: 返回已经注册过的邮箱地址, 或者抛出错误.

#### clean_password

type: function

paramters: self

return_type: str

description: 检测用户提供的密码是否合法. 如果是, 返回密码, 否则抛出`ValidationError`错误.

pre-condition: `self.cleaned_data`中含有`password`键.

post-condition: 返回合法的密码, 或者抛出错误.

#### clean_repeated_password

type: function

paramters: self

return_type: str

description: 检测用户提供的密码是否合法, 两次提供的密码是否一致. 如果是, 返回密码, 否则抛出`ValidationError`错误.

pre-condition: `self.cleaned_data`中含有`password`和`repeated_password`键.

post-condition: 返回合法的密码, 或者抛出错误.

#### clean_username

type: function

paramters: self

return_type: str

description: 检测用户提供的用户名是否合法且未被注册. 如果是, 返回用户名, 否则抛出`ValidationError`错误.

pre-condition: `self.cleaned_data`中含有`username`键.

post-condition: 返回合法的用户名, 或抛出错误

## email_send

### random_str

type: function

paramters: random_length=8: int

return_type: str

description: 返回random_length位的随机字符串. 该字符串中仅包含大小写字母和数字.

pre-condition: 无

post-condition: 如果random_length是int类型, 返回生成的随机字符串. 否则, 抛出`TypeError`错误.

### send_code_email

type: function

paramters: email: str, send_type: str

return_type: bool

description: 给email地址发送验证码邮件

pre-condition: 可以通过EmailVerifyRecord类创建对象

post-condition: 尝试向email发送邮件并返回尝试结果.
