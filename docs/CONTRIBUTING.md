# Contributing to RTI Project

Thank you for your interest in contributing to the RTI robotics project! 
This guide will help you get set up and understand how to contribute effectively.

---

## Getting Started: Environment Setup

Before contributing, make sure your system is ready.
Follow the full setup instructions in [docs/setup.md](./setup.md)

This includes:
- Installing ROS 2 Humble
- Cloning the project
- Installing Gazebo and ROS 2 dependencies
- Building the workspace with `colcon`
---

## Branching Strategy

Use short, descriptive branch names based on the type of work:

- `feature/<name>` – for new features
  _Example_: `feature/cv-classification-node`
- `fix/<bug>` – for bug fixes
  _Example_: `fix/agv-collision-logic
- `chore/<task>` – for non-code or maintenance tasks
  _Example_: `chore/update-readme`

Always branch off the latest `main`:

```bash
git checkout main
git pull origin main
git checkout -b feature/<your-branch-name>
```

---
## Submitting a Pull Request

1. Make changes and commit:
    ```bash
    git add .
    git commit -m "feat: your descriptive commit message"
    ```

2. Push your branch:
    ```bash
    git push origin feature/<your-branch-name>
    ```

3. Open a pull request on GitHub
    - Use the pull request template (auto-filled)
    - Request reviews from collaborators
    - Link to related Issues (e.g. Closes #12)
    - Wait for reviews and approvals
    - Merge after approval (if you’re the PR author)


4. Contribution Etiquette
     - Keep PRs focused and atomic
     - Prefer smaller PRs over huge all-in-one changes
     - Document code and update README or launch files if needed
     - Ask questions via GitHub Discussions or tag teammates in PRs

---

## Code Standards & Linting

- Use `pre-commit` hooks to auto-check formatting (coming soon)
- Follow ROS 2 best practices for structure and naming
- Include tests and launch files when appropriate

---

## Testing

After building, run tests:

```bash
colcon test
colcon test-result --verbose
```
---

## Thanks!

We appreciate your contribution to open-source robotics! 
