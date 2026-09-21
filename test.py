import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title = "测试",
    page_icon = "random",
    # 布局
    layout = "centered",
    # 控制的是侧边栏的状态
    initial_sidebar_state = "expanded",
    menu_items = {
        'Get Help' : 'https://docs.streamlit.io/',
        'Report a bug' : "https://docs.streamlit.io/",
        'About' : '# 恭喜你发现了这个网页！'
    }
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("测试")
st.write("现在是2026/08/06 18:01")
st.write("我写下了这一段文字")
st.write("现在在学python，教学是在b站找的黑马程序员的课程，很不错，适合小白，值得推荐")
st.write("好了，现在请静静欣赏我磕的cp与她们的美照")

# 图片
st.image("resources/sua.png")
st.image("resources/mizi.png")
st.image("resources/DayNight.jpg")

# 音频
st.write("sua单曲")
st.audio("resources/suaSing.mp3")
st.write("mizi单曲")
st.audio("resources/miziSing.mp3")
# 视频
st.video("resources/ZombieStageR1.mp4")

# logo
st.logo("resources/ice.jpg")

# 表格
st.write("两位的主线，包含异形舞台与血鬼舞台")
story = {
    "视频" : ["铁线莲", "MIZ&SUA", "KARMA", "Candy Scar"],
    "主唱" : ["sua & mizi", "纯音乐", "mizi", "sua & mizi"],
    "时间": ["2023-03-29", "2023-08-27", "2025-06-27", "2026-06-26"],
    "时长": ["4分9秒", "2分4秒", "8分5秒", "5分6秒"]
}
st.table(story)

st.write("两位的歌曲")
music = {
    "视频" : ["Prologue 甜梦","Black Sorrow", "Ruler of my heart", "CURE", "Heart", "Witch", "wiege", "BOnBon水母星", "MirroR", "Unknown Till The End", "All In"],
    "主唱" : ["sua", "mizi", "sua", "sua & mizi", "sua", "mizi", "sua & mizi", "sua", "mizi", "Sua", "Mizi"],
    "时间": ["2023-04-04", "2024-01-02", "2024-10-01", "2025-04-23", "2025-09-04", "2025-10-08", "2025-11-05", "2026-01-08", "2026-06-26", "2026-09-19", "2026-09-19"],
    "时长": ["1分48秒", "3分40秒", "4分9秒", "3分13秒", "3分22秒", "4分5秒", "3分4秒", "3分11秒", "5分6秒", "2分10秒", "3分4秒"]
}
st.table(music)

# 输入框
# 普通输入框
wish = st.text_input("请输入祝福语")
st.write(f"您给出的祝福语为：{wish}")

#密码输入框
password = st.text_input("请输入不想暴露的话,此输入框无法输入中文", type = "password")
st.write(f"我要揭露你的话！你打出来的话是：{password}")

# 单选按钮
star = st.radio("请选择你的方向",["mizi", "sua", "sua & mizi", "misu", "sumi"])
st.write(f"您选择的方向为：{star}")
