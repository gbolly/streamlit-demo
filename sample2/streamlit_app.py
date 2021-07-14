# -*- coding: utf-8 -*-
# Copyright 2018-2019 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st


# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# Hide the streamlit menu per https://discuss.streamlit.io/t/how-do-i-hide-remove-the-menu-in-production/362/10
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


"""**An example showing the square of value.**"""

value = st.slider('Select a VALUE')
st.write("**%i** squared is **%i**" % (value, value * value))
