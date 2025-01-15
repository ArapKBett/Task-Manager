```
This project is an AI-driven task management tool designed to predict task durations, suggest optimizations, and automate task assignments to improve productivity.

## Project Structure

```
project_directory/
│
├── AI_Task_Management/
│   ├── task_manager.py
│   ├── task_manager.html
│   └── app.py
```

### Files

- **task_manager.py**: Contains functions to predict task durations, suggest optimizations, and automate task assignments using OpenAI's GPT-3.
- **task_manager.html**: Provides a simple web interface for interacting with the task management tool.
- **app.py**: A Flask server that handles API requests from the frontend and interacts with the task management functions.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries: `flask`, `openai`
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ArapKBett/Task-Manager
   cd ai-task-management
   ```

2. Install the required libraries:
   ```bash
   pip install flask openai
   ```

3. Set up your OpenAI API key:
   - Sign up for an API key at [OpenAI](https://beta.openai.com/signup/).
   - Replace `'your_openai_api_key'` in `task_manager.py` with your actual API key.

### Usage

1. Run the Flask server:
   ```bash
   python app.py
   ```

2. Open `task_manager.html` in your web browser to access the AI Task Management Tool.

3. Use the web interface to:
   - Predict task durations by entering a task description and clicking "Predict Duration".
   - Suggest optimizations for a task by entering a task description and clicking "Suggest Optimizations".
   - Automate task assignments by clicking "Automate Assignments".

### Example

1. **Predict Task Duration**:
   - Enter a task description (e.g., "Develop a new feature for the application").
   - Click "Predict Duration".
   - The predicted duration will be displayed.

2. **Suggest Optimizations**:
   - Enter a task description (e.g., "Develop a new feature for the application").
   - Click "Suggest Optimizations".
   - Suggested optimizations will be displayed.

3. **Automate Assignments**:
   - Click "Automate Assignments".
   - Automated task assignments will be displayed.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for providing the GPT-3 A
