from collections import namedtuple
import altair as alt
import math
import pandas as pd
from crewai import Agent, Task, Crew, Process
import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.image('images/crew_logo.png')

st.text('This is some text')