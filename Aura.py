import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from plot import plot_distribution,plot_finalscore_distribution
sns.set(style='darkgrid',palette = 'Set2')
# Apply the orange theme
#st.markdown(orange_theme, unsafe_allow_html=True)
# Load data
df = pd.read_csv('combined3jan29.csv')

st.title('Weld Process Distribution Analysis')

plot_distribution(df,'WELDPROCESS', 'Distribution of  Weld Processes')
st.pyplot(plt)

selected_weld_process = st.selectbox('Select Weld Process', ['GMAW', 'SMAW', 'GTAW', 'FCAW'], index=1)

st.write(f"Selected Weld Process: {selected_weld_process}")
gmaw_df = df[df['WELDPROCESS'] == selected_weld_process]
plot_distribution(gmaw_df, 'JOINTTYPE', f'Distribution of jointype (BUTT, TEE, LAP) in {selected_weld_process}')
st.pyplot(plt)

selected_joint_type = st.selectbox('Select Joint type', ['BUTT', 'TEE', 'LAP',], index=1)
st.write(f"Selected Weld Process: {selected_joint_type}")
gmaw_butt_df = gmaw_df[gmaw_df['JOINTTYPE'] == selected_joint_type]

plot_distribution(gmaw_butt_df,'WELDPOSITION',f'Distribution of jointype (BUTT, TEE, LAP) in {selected_weld_process}and in  {selected_joint_type}')
st.pyplot(plt)

a = gmaw_butt_df['WELDPOSITION'].unique()

selected_joint_position_type = st.selectbox('Select Joint WELDPOSITION type', a, index=1)
st.write(f"Selected Weld Process: {selected_joint_position_type}")
gmaw_butt_join_df = gmaw_butt_df[gmaw_butt_df['WELDPOSITION'] == selected_joint_position_type]

# plot_distribution(gmaw_butt_join_df,'WELDPOSITION',f'Distribution of jointype (BUTT, TEE, LAP) in {selected_weld_process}and in{selected_joint_type} in {selected_joint_position_type} position ')
# st.pyplot(plt)
unique_df = gmaw_butt_join_df.groupby(['LESSON_NUM','result'])['USERNAME'].nunique().reset_index()
plt.figure(figsize = (8,5),dpi= 300)
order = ['pass', 'fail']
ax = sns.barplot(x='LESSON_NUM', y='USERNAME', hue='result',
                 data=unique_df,hue_order =['pass'])
ax.bar_label(ax.containers[0]);
plt.title('Lesson Performance')
plt.xlabel('Lesson Number')
plt.ylabel('Total Usernames')
plt.legend(title='Result', loc='upper right')
plt.show()
st.pyplot(plt)
