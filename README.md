***京急の運行情報ページに変更があったため、現在このライブラリは利用できません***
***近日中に対応予定です***


# KeikyuPython


![KeikyuPython by pokiiio ( ポキオ )](https://lh3.googleusercontent.com/XqO5bdZ3l6-KzxyaxcuxSQnOEjFxdzVoTHL3d5A392PP8B_9CBs6hGUNSiHe_TyHMOL9GveXkE2ZgnOMAPMYQgZH52oAe9E1_zBJSHengeKl0OsJsKkImIm-xLEDa_eYNJKZ1lFNIRU=s600 "KeikyuPython by pokiiio ( ポキオ )")


京急の運行情報を取得するPythonモジュールです。

京急の運行情報のページから運行情報の文字列をパースします。



## 使い方

`keikyu.py`をダウンロードやクローンして、運行情報を取得したいPythonスクリプトと同じディレクトリに保存してください。


```python
import keikyu

print keikyu.get_unko()
```


`keikyu.get_unko()`で運行情報の文字列を取得できます。


## 注意

`unko`とは運行のことを指しています。
