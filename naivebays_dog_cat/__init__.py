from naivebays_dog_cat.niavebayes_naver_movie import NaiveBayesClassfier
context = './data/'
model = NaiveBayesClassfier()
model.train(context+'review_train.csv')
# print(model.classfy('내 인생에서 쓰레기 같은 영화'))
# print(model.classfy('내 인생에서 최고의 영화'))
# print(model.classfy('내 인생에서 그저그런 영화'))
# print(model.classfy('내 인생에서 볼 만한 영화'))
# print(model.classfy('내 인생에서 다시는 보고싶지 않은 영화'))
# print(model.classfy('내 인생에서 죽기전에 꼭 한번쯤은 다시 봐야할 영화'))
print(model.classfy('망작'))


