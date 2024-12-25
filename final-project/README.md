# Assignment Submission Guidelines

Follow the steps below to complete and submit your assignment correctly.

## Steps for Submission

1. **Fork the Repository**  
   Start by forking the main repository to your GitHub account.

2. **Clone the Repository**  
   Clone the forked repository to your local machine. Use the following command:
   ```bash
   git clone <your-forked-repo-url>
   ```

3. **Create a Branch**  
   Create a new branch for your submission. Name it using your project or name for clarity:
   ```bash
   git checkout -b <your-branch-name>
   ```

4. **Add Your Code**  
   Inside the `final-project` folder, create a new folder with your name. Add your project files inside this folder. The folder structure should look like this:
   ```
   final-project/
   └── your-name/
       ├── app.py
       ├── README.md
       ├── requirements.txt
       ├── Dockerfile
       ├── templates
       └── any-other-files-or-folders
   ```

5. **Document Your Work**  
   - Include a `README.md` in your folder explaining:
     - What your project does.
     - How to run it.
     - Where you have hosted the project (if you have a live url, please include that).
     - Any dependencies or special instructions.
   - Add a `requirements.txt` file if your project has Python dependencies.

6. **Commit Your Changes**  
   Add your changes to the staging area and commit them:
   ```bash
   git add .
   git commit -m "Add final project for <your-name>"
   ```

7. **Push Your Branch**  
   Push your branch to your forked repository:
   ```bash
   git push origin <your-branch-name>
   ```

8. **Create a Pull Request**  
   Go to the original repository on GitHub and create a pull request (PR) from your branch. Include a meaningful title and description for your PR.

## Example Code Snippets

### Example Folder Structure
```
final-project/
└── john-doe/
    ├── app.py
    ├── README.md
    ├── requirements.txt
    ├── Dockerfile
    └── templates/
        └── index.html
```

### Example `README.md`
```markdown
# My Final Project

## Description
This project implements a simple web app in flask.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the main script:
   ```bash
   flask run app.py
   ```
### Example `requirements.txt`
```
requests==2.28.2
flask==2.3.0
```

---

If you have any questions or run into issues, feel free to reach out for help! 
