import gradio as gr

CV_path = "Tsovinar_Babakhanyan_CV.pdf"

with gr.Blocks(title="Tsovinar Babakhanyan",theme = gr.themes.Soft(primary_hue = "blue", secondary_hue = "green", font=["Inter","system-ui","sans-serif"])) as demo:
    gr.Markdown("""# 👩🏻‍💻 Tsovinar Tina Babakhanyan 
                 ### Data scientist | Machine Learning & NLP Engineer
                    
                📍 Armenia • ✉️ Tsovinar.babakhanyan@hotmail.com  
    🔗 [GitHub](https://github.com/Tsovinar1986) • [DAGsHub](https://dagshub.com/Tsovinar1986)
    """)
    with gr.Row():
        with gr.Column(scale =2):
            gr.Markdown("""
                ### 🧠 Professional Summary
            Data Scientist and Junior Machine Learning Engineer with hands-on experience in  
            **NLP, LLMs, and real-world AI projects**.  

            Worked on multilingual NLP, chatbots, and data analytics through  
            **Omdena and startup environments**.
            """)
        with gr.Column(scale =1):
            gr.Markdown("""
            ### 🌍 Languages
            - Armenian – Native  
            - English – Advanced  
            - Russian – Intermediate
            """)
            
    gr.Markdown("---")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ### 🛠 Technical Skills
            **Languages:** Python, SQL  
            **ML / AI:** NLP, LLMs, Transformers  
            **Frameworks:** PyTorch, TensorFlow, Hugging Face  
            **LLM Tools:** LangChain, CrewAI  
            **Data:** Pandas, NumPy, GeoPandas, QGIS  
            **CV:** OpenCV  
            **Web:** Flask, Django (basic)  
            **Tools:** Git, GitHub, Azure DevOps, Jira, TestRail
            """)
        with gr.Column():
            gr.Markdown("""
            ### 💼 Experience

            **Omdena – Junior ML Engineer**  
            *Oct 2024 – Dec 2024*
            - NLP & LLM-based WhatsApp chatbots  
            - Image & text preprocessing  
            - OpenCV-based classification  

            **Oragic Startup – Data Science Intern**  
            *Sep 2022 – Dec 2023*
            - Multilingual NLP research  
            - Sentiment analysis models
            """)
    gr.Markdown("---")
    
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("""
            ### 📜 Certifications
            - Product Owner – Omdena  
            - Data Engineer – Omdena  
            - AI Innovation Challenge  
            - Text Summarization – Omdena  
            - QA Methodologies  
            - Python Developer & ML
            """)
    
    gr.Markdown("---")
    
    gr.File(
        value=CV_path,
        label="📄 Download PDF CV",
        interactive=False
    )
demo.launch(share=True)
            

    
            