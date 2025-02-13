# Sophia Automata

## AI-Powered Research Automation System

This project integrates multiple backend services and a frontend application to provide a comprehensive solution for research paper analysis, resource gathering, and streamlined note-taking. By combining the **CrewAI** framework (for AI-driven workflows), the **Exa API** (for neural-powered web search), and **OpenAI-based agents**, it automates literature review, source selection, and rapid summarization of research content.

One of the core features is a **2-window workspace**:
1. **Window 1**: Automatically opens **3 research links** and **2 educational videos**.
2. **Window 2**: Opens a **Google Doc** containing a summary, analysis, and an organized note-taking guide based on the provided sources.

This approach significantly enhances the research experience by making it easier to gather relevant materials, analyze their contents, and keep organized notes. A short demonstration video is available on YouTube showcasing these capabilities:

[Watch the Demo](https://www.youtube.com/watch?v=np8-3EnTRiY&ab_channel=PragathSiva)

---

## Backend

### Modules

1. **Browser Automation**  
   - Manages the initialization of a browser instance and automatically opens two windows:
     - Window 1 with research links and educational videos.
     - Window 2 with a Google Doc for summarizing and note-taking.
   - See code: [Backend/browser.py](Backend/browser.py)

2. **Research Topic Analysis**  
   - Receives research topics and returns relevant articles and videos using a system of custom AI agents.
   - Leverages the **Exa API** for neural-powered web search and the **CrewAI** framework for orchestrating tasks.
   - See code: [Backend/crew_sources.py](Backend/crew_sources.py)

3. **Content Summarization**  
   - Analyzes and summarizes text content using **OpenAI's GPT** models.
   - Outputs the summary to both the user and a text file (and also populates the Google Doc).
   - See code: [Backend/analyze.py](Backend/analyze.py)

### Configuration

- **Agents** and **tasks** are configured through YAML files for easy customization.
  - Agent configuration: [Backend/config/agents.yaml](Backend/config/agents.yaml)
  - Task configuration: [Backend/config/tasks.yaml](Backend/config/tasks.yaml)

### Dependencies

- The project requires Python libraries listed in `requirements.txt`.
- See dependencies: [Backend/requirements.txt](Backend/requirements.txt)

---

## Frontend

### Features

1. **Paper Submission Form**  
   - Allows users to input the title and content of their research paper.
   - See component: [Frontend/src/components/PaperInputForm.tsx](Frontend/src/components/PaperInputForm.tsx)

2. **Results Display**  
   - Displays links to relevant articles and educational videos as cards.
   - See component: [Frontend/src/components/ResultCard.tsx](Frontend/src/components/ResultCard.tsx)

3. **Search Functionality**  
   - Provides a search bar for quick topic searches.
   - See component: [Frontend/src/components/SearchBar.tsx](Frontend/src/components/SearchBar.tsx)

### Technologies

- **React** and **TypeScript** for building the user interface.
- **Tailwind CSS** for styling.
- Configuration for TypeScript and Vite in their respective config files.

### Setup

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

3. Build for production:
   ```bash
   npm run build
   ```

## Getting Started

To get a local copy up and running follow these simple steps:

1. Clone the repo:
   ```bash
   git clone https://your-repository-url.git
   ```

2. Install backend dependencies:
   ```bash
   pip install -r Backend/requirements.txt
   ```

3. Start the backend server:
   ```bash
   python Backend/main.py
   ```

4. Install frontend dependencies and start the frontend server as described in the Setup section above.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Pragath Siva - pragathtsiva@gmail.com

Project Link: [[https://github.com/yourusername/your-repo](https://github.com/yourusername/your-repo](https://github.com/PragathTSiva/Sophia-Automata.git))
