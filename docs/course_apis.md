## views

### GetLearnModel

type: class

father: `rest_framework.generics.GEnericAPIView`

#### get

type: function

paramters: self, request

return_type: JsonResponse

description: 如果传入的请求使用GET方法, 使用Manager接口查询, 序列化并返回learn模板需要的的数据. 它包含`category_list`和`ad_info`两个字段.

pre-condition: 无

post-condition: 返回JsonResponse对象

### GetDiscoverModel

type: class

father: `rest_framework.generics.GEnericAPIView`

#### get

type: function

paramters: self, request

return_type: JsonResponse

description: 如果传入的请求使用GET方法, 使用Manager接口查询, 序列化并返回discover模板需要的的数据. 它包含`viewpager_info`, `new_videos_info`和`popular_videos_info`三个字段.

pre-condition: 无

post-condition: 返回JsonResponse对象

### GetStartPageModel

type: class

father: `rest_framework.generics.GEnericAPIView`

#### get

type: function

paramters: self, request

return_type: JsonResponse

description: 如果传入的请求使用GET方法, 使用Manager接口查询, 序列化并返回Learn模板需要的的数据. 它包含`image_url`一个字段.

pre-condition: 无

post-condition: 返回JsonResponse对象

### GetVideoPlayerModel

type: class

father: `rest_framework.generics.GEnericAPIView`

#### get

type: function

paramters: self, request

return_type: JsonResponse

description: 如果传入的请求使用GET方法, 使用Manager接口查询, 序列化并返回Learn模板需要的的数据. 它包含`video_sugestion_info`和`video_info`两个方法.

pre-condition: 无

post-condition: 返回JsonResponse对象

## models

### VideoModel

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ video_title
+ video_level
+ video_cover
+ video_url
+ video_author
+ video_reference
+ submission_date
+ video_description
+ video_heat
+ user

### Sentence

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ video
+ sentence_content
+ sentence_English
+ sentence_pronunication
+ sentence_pinyin
+ word
+ user

### Grammar

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ grammar_content
+ grammar_example1
+ grammar_example2
+ sentence

### Word

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ word_content
+ word_spelling
+ word_meaning
+ word_spell_url
+ user

### Category

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ category_cover
+ category_title
+ category_description
+ category_author
+ category_total

### Advertisement

type: class

father: `django.db.models.Model`

description: 保存视频信息的类.

fields:

+ ad_cover
+ ad_url

## serializers

type: class

father: `rest_framework.serializers.ModelSerializer`

### VideoSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type:class

fields:

+ model
+ exclude

### SentenceSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### GrammarSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### WordSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### StarSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### UserSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### CategorySerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### AdvertisementSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ exclude

### VideoBasicSerializer

type: class

father: `rest_framework.serializers.ModelSerializer`

#### Meta

type: class

fields:

+ model
+ fields

