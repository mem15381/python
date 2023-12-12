from parsivar import Tokenizer
from parsivar import POSTagger

my_tokenizer = Tokenizer()
my_tagger = POSTagger(tagging_model="wapiti")  # tagging_model = "wapiti" or "stanford". "wapiti" is faster than "stanford"
text_tags = my_tagger.parse(my_tokenizer.tokenize_words("ی و غیرشبکه ای با استفاده از نرم افزار و از طریق فضای مجازی، فعالیت و ارائه خدمات و کالا در فضای مجازی به صورت مستقیم یا با واسطه ، خرید و فروش اینترنتی انواع کالا و خدمات مجاز از طریق ایجاد و راه اندازی وب سایت و یا برقراری ا"))
print(text_tags)
with open('tag.txt', 'w') as f:
    f.write(text_tags)