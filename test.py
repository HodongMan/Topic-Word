from konlpy.tag import Twitter
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations


measures = collocations.BigramAssocMeasures()
doc = "턴 에는 청소년 문제뿐만이 아닌 여러가지 복합적인 사회문제들이 간접적으로 제시되어있었다.  프로 작가들이 풀어내는 이야기들이라 첫 장을 펴면서 저도 모르게 이상한 나라의 앨리스처럼 끝장까지 스르륵 빠져든다는 게 이 책의 매력이다. 내가 가장 걱정하고 신경썼던 부분은 소율과 지아의 신경전, 그로인해 행해지는 사이버폭력이다. '혀 밑에 칼이 있다.' 라는 속담이있다. 하지만 이것도 옛 말이다. 클릭 한 번에 칼날이 비수로 꽂힌다 라는 말이 새로 생겨야한다. 누군가를 향한 정확하지 않은 사실에 대한 마구잡이 유포, 질투를 가장한 언어폭력은 현재 내가 이 글을 쓰고 있는 현실에서도 수없이 행해지는 사이버폭력들이다. 마음 연약한, 연한 녹색 새싹같은 아이들의 마음에 생채기를 내는 이런 사이버폭력들을 막으려면 어떻게 해야할까...? 다른 부분들도 의미깊고 재미있었지만 나는 이 부분이 가장 걱정되고, 개선하고 싶은 부분이라 생각한다. 강력한 인터넷 실명제를 도입하여 아예 사진까지도입하여 제 얼굴을 걸고 댓글을 쓰도록 만들어야하지 않을까 생각한다.생각없는 클릭질에 가슴에 피가 철철 흐르지 않도록 그렇게 되어야 한다....! 세용의 이야기도 의미깊고 기대가 되었다. 타인에 의해 이루어지는 변화는 어디까지일까. 한 사람으로 인해 변할 수 있는 세용의 넓이와 깊이가 궁금하다. 청소년연작소설 [뜨인돌] 턴 정말 매력있고 생각할 거리를 주는 좋은 청소년 소설이었다. 내가 한 행동은 미래에 누군가가 나에게 할 수 있는 행동이다. 모든 것은 연결되어있다. 좋은 것은 좋은 것과, 혹은 나쁜 것과..그렇지만 나쁜것과 연결된 것은 전에 내가 했던 좋았던 행동으로 상쇄시킬 수 있다. 뫼비우스의 띠처럼 우리는 같은, 이어진 고리를 끊임없이 순환하는 것은 아닐까. 간만에 독서 열심히 한 것 같다. 지루하지 않게, 생감있게, 현실을 바로 볼 수 있을 수 있었던 좋은 책이었다."

print('\nCollocations among tagged words:')
tagged_words = Twitter().pos(doc)
finder = collocations.BigramCollocationFinder.from_words(tagged_words)
print(finder.nbest(measures.pmi, 10)) # top 5 n-grams with highest PMI



print('\nCollocations among words:')
words = [w for w, t in tagged_words]
ignored_words = [u'안녕']
finder = collocations.BigramCollocationFinder.from_words(words)
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
finder.apply_freq_filter(3) # only bigrams that appear 3+ times
pprint(finder.nbest(measures.pmi, 10))

print('\nCollocations among tags:')
tags = [t for w, t in tagged_words]
finder = collocations.BigramCollocationFinder.from_words(tags)
pprint(finder.nbest(measures.pmi, 5))
