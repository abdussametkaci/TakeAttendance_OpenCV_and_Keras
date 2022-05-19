# TakeAttendance_OpenCV_and_Keras
## Öğrenci yoklaması alan program
Bu program sınıfa giren öğrencilerin yüzlerini tespit ederek kimlerin sınıfta olduğunu tespit eden bir programdır. 

## Programın Ana Mantığı
Programı yazarken öncelikli olarak Keras kütüphanesi kullanarak deep learning methodunu ile modelimi eğittim. Bu projeyi yaparken tüm sınıf arkadaşlarımın fotoğraflarını alamayacağım için kendi ve 2 arkadaşımın fotoğraflarını aldım (yüzlerce fotoğraf var).

Daha sonra bu adlığım fotoğraflarda OpenCV ile yüzleri tespit edip DataSet2 adlı bir klasör açıp oraya kayıt ettim. Yüzleri kayıt ederken direkt olarak kayıt etmiyorum. Resimleri siyah beyaz olarak kaydediyorum. Bunun nedeni de renkli resimler 3 adet matris içerirken siyah beyaz resmiler ise 1 adet matris içeriri. Eğitim sırasında daha az enerji ve daha az zamanın harcanmasını sağlar. Daha sonra ise modelimi eğitmeden önce genelde data setlerninin 1/3'ü test ve 2/3'ü ise train olarak ayrılır. Ben de bu işlmeleri SplitData klasörü açıp oraya kaydettim. En sonunda da datalarımı ayıkladıktan sonra dataset'imi eğittim. Eğittim bu modeli de kameradaki yüzler ile karşılaştırark kimin sınıfta olduğunu tespit ederek yoklama için açtığım textfield'a öğrencinin adını yazmaktadır. 

Daha ayrıntılı bilgi için projenin anlatıldığı link: https://www.youtube.com/watch?v=zqos3TLVm0E&t=228s
