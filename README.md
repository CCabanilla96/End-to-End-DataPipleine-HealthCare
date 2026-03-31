# End-to-End-DataPipleine-HealthCare
This project demonstrates a complete end-to-end data pipeline for healthcare data, covering data ingestion, processing, storage, and visualization. The pipeline extracts datasets from Kaggle using the Kaggle API, processes and transforms the data using Python and Pandas, and loads it into a PostgreSQL relational database for structured storage and querying. Finally, the data is connected to Power BI to build interactive dashboards and uncover actionable insights.

The project is designed to simulate a real-world data engineering workflow, emphasizing reproducibility, modular design, and scalability. It showcases the integration of multiple tools and technologies across the data lifecycle, from raw data acquisition to business intelligence reporting.

Key objectives of this project include:

Automating data ingestion from external sources (Kaggle)
Performing data cleaning and transformation using Python
Designing and managing a relational database in PostgreSQL
Loading and structuring data for efficient querying
Connecting the database to Power BI for visualization and reporting
Delivering insights through interactive dashboards focused on healthcare metrics

This project highlights practical skills in data engineering, database management, and data visualization, demonstrating the ability to build and operationalize a full data pipeline from start to finish.

Following programs utilized for this project includes:

-Python

-Pandas

-PostgreSQL

-Kaggle API

-Power BI

-VS Code

Pipeline flow:
Kaggle API → Python (Pandas) → PostgreSQL → Power BI

The data pipeline follows a structured, end-to-end workflow that transforms raw healthcare data into actionable insights through automation and integration across multiple tools.

The process begins with securely obtaining and configuring an API key from the Kaggle platform, enabling programmatic access to external datasets. Using a Python-based ingestion script developed in Visual Studio Code, the pipeline connects to the Kaggle API and retrieves the required data.

Once extracted, the data is ingested and processed using Python and the Pandas library, where it can be cleaned, structured, and prepared for downstream use. The processed dataset is then loaded into a relational database built with PostgreSQL, enabling efficient storage, querying, and data management.

Finally, the database is connected to Microsoft Power BI, where interactive dashboards and visualizations are created to analyze healthcare trends and support data-driven decision-making.

