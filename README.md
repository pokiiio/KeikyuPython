# KeikyuPython
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
