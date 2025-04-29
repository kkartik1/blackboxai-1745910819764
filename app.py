import streamlit as st
from file_upload import upload_file
from data_processing import process_data, categorize_variables, correct_categorization
from visualization import generate_visualizations
from ai_agent import OllamaAgent
from feedback import handle_feedback

def main():
    st.title("Healthcare Claims Data Visualization")

    # Step 1: Upload file
    uploaded_file = upload_file()

    if uploaded_file is not None:
        # Step 2: Process and categorize variables
        df = process_data(uploaded_file)
        variable_info = categorize_variables(df)

        # Step 3: Allow user to correct categorization
        corrected_info = correct_categorization(variable_info)

        # Step 4: Suggest visualizations based on corrected categorization using Ollama AI
        agent = OllamaAgent()
        suggested_viz = agent.suggest_visualizations(corrected_info)

        # Display suggested visualizations and get user selection
        selected_viz = st.multiselect("Select visualizations to generate", suggested_viz)

        # Step 5: Generate interactive visualizations
        if selected_viz:
            generate_visualizations(df, corrected_info, selected_viz)

        # Step 6: Reinforcement learning with user feedback
        feedback = st.text_area("Provide feedback on the visualizations")
        if st.button("Submit Feedback"):
            agent.update_with_feedback(feedback)
            handle_feedback(feedback)

if __name__ == "__main__":
    main()
