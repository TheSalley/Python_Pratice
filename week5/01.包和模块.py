"""
    包就是文件夹，里面可以嵌套包
    一个python 文件就是一个模块

    __init__.py 是python 包里必须存在的文件，等同于身份证

    包的导入：
        import package

    示例：
        python 解释器环境下在终端
        输入 import animal
            animal_test()

    模块的导入：
        form package import module

    示例：
        输入 from animal.cat import action
            action.run()

            from animal.cat import action as cat_action  # 起别名
"""
