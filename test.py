from konlpy.tag import Twitter
from konlpy.corpus import kolaw
from konlpy.utils import pprint
from nltk import collocations


measures = collocations.BigramAssocMeasures()
doc = "이런 글을 쓴 이유는 쫄쫄 굶는 아일랜드 서민들을 위해서 아무것도 안 해주는 현실을 비꼬기 위해서다. 당연하지만 스위프트가 저걸 실제로 실행할 정도로 미친 인간은 절대 아니다. 무엇보다 스위프트는 아일랜드 출신이다!!!으로 자신의 소설 걸리버 여행기 라퓨타편에서 라퓨타에 항거해 독립을 쟁취하는 린달리노(Lindalino)라는 도시를 통해 아일랜드의 독립을 간접적으로 주장하다가 초판에서 편집당한 전적이 있었다. \r\n\r\n이런 점에서 다시 앞의 내용을 제대로 해석해보자면 \"아일랜드 사람들 다 죽게 생겼다. 이럴바엔 차라리 죽여라 영국놈들아.\"정도로 해석이 가능하며 위에서 언급한 걸리버 여행기와 더불어 블랙코미디의 원조같은 글이다. 어쨌건 파격적인 내용 덕분에 현대에도 많이 인용되는 수필이기도 하다. \r\n\r\n아일랜드 대기근 당시 상황을 풍자한 것으로 알려져 있기도 하나, 저작 연도를 보면 알 수 있듯이 100년 전에 나온 글이다. 다만 영국과 아일랜드 간의 나아질래야 나아질 수가 없는 관계를 설명하는데 좋은 글이긴 하다. 그리고 이 글이 쓰여진 뒤에도 아일랜드의 사정은 전혀 나아지지 않았다. 더 나빠지면 나빠졌지. 실제로 100년 뒤 대기근 때는 진짜로 사람을 수출(?)[1]하기 시작했다. 이것 때문에 아일랜드 인구는 기근전 900만명에서 절반넘게 이민가거나 아사해버려서 현재에도 아일랜드섬 전체의 인구는 600만명을 간신히 넘긴다. \"셋 중 하나는 죽고, 하나는 이민가고, 하나만 남았다\"고 보면 된다. \r\n\r\n여담이지만 잭 톰슨의 겸손한 게임 제안은 이 수필에서 이름을 딴 것이다. 물론 이름만 딴 거지 내용은 형편없다."
tagged_words = Twitter().pos(doc)

words = [w for w, t in tagged_words]
ignored_words = [u'안녕']
finder = collocations.BigramCollocationFinder.from_words(words)
finder.apply_word_filter(lambda w: len(w) < 2 or w in ignored_words)
finder.apply_freq_filter(3) # only bigrams that appear 3+ times
result = finder.nbest(measures.pmi, 10)
print(result)