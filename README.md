# chinese_rapper_tool

1. 如果想找押韵词，并且需要音调完全一致 ，用word_finder_tone.py。 修改target_suffix，比如词语”解药“， 改成
    target_suffix = ["ie3", "ao4"]
    Jie 舍弃j， 第三声所以是ie3， Yao舍弃y， 第四声所以是“ao4”。
2. 如果只想找押韵词， 不在意音调一致， 用word_finder.py， 修改target_suffix，比如词语”解药“， 改成
    target_suffix = [ 'ie', 'ao']

