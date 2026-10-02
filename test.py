import streamlit as st
import streamlit.components.v1 as components

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

# 1. 初始化状态
if "egg_welcome_shown" not in st.session_state:
    st.session_state.egg_welcome_shown = False


# 2. 定义弹窗内容
@st.dialog("🎉 彩蛋房间！")
def welcome_dialog():
    st.write("恭喜你到达此处！")
    st.write("这是跟着老师第一次接触streamlit时做的")
    st.write("那么，祝你玩的开心！")

    # 弹窗里的跳转链接
    st.link_button("返回", "https://icetest-e332jnxmr2nipb896ruhss.streamlit.app/")

    # 关闭弹窗的按钮
    if st.button("进入房间"):
        st.session_state.egg_welcome_shown = True
        st.rerun()


# 3. 判断是否弹出
if not st.session_state.egg_welcome_shown:
    welcome_dialog()
    st.session_state.egg_welcome_shown = True

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
st.image("https://img-reg-ab.imagency.cn/a/272/26/6abfa403e5c18.png")
st.image("https://img-reg-ab.imagency.cn/a/272/26/6abfa3c570243.png")
st.image("https://img-reg-ab.imagency.cn/a/272/26/6abfa4d83ae2c.jpg")

# 音频
st.write("sua单曲")
st.audio("https://mp3tourl.com/audio/1790945854231-67d5f143-5413-4e8f-9023-754cc713c318.mp3", format="audio/mp3")
st.write("mizi单曲")
st.audio("https://mp3tourl.com/audio/1790945939558-14dafbac-f421-4c48-92ee-d129da3b9b31.mp3", format="audio/mp3")
# 视频
bilibili_url = "https://player.bilibili.com/player.html?isOutside=true&aid=116815359379487&bvid=BV1km736DE9j&cid=39421870900&p=1"
components.iframe(bilibili_url, height=500)

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
    "视频" : ["Prologue 甜梦","Black Sorrow", "Ruler of my heart", "CURE", "Heart", "Witch", "wiege", "BOnBon水母星", "MirroR", "Unknown Till The End", "All In", "Sweet Dream(Extended)"],
    "主唱" : ["sua", "mizi", "sua", "sua & mizi", "sua", "mizi", "sua & mizi", "sua", "mizi", "sua", "mizi", "sua"],
    "时间": ["2023-04-04", "2024-01-02", "2024-10-01", "2025-04-23", "2025-09-04", "2025-10-08", "2025-11-05", "2026-01-08", "2026-06-26", "2026-09-19", "2026-09-19", "2026-10-02"],
    "时长": ["1分48秒", "3分40秒", "4分9秒", "3分13秒", "3分22秒", "4分5秒", "3分4秒", "3分11秒", "5分6秒", "2分10秒", "3分4秒", "3分30秒"]
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
