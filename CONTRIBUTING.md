# 🤝 Contributing to WhatsApp Medical AI Chatbot

Thank you for your interest in contributing! This guide will help you get started with contributing to our medical chatbot project.

## 🌟 Ways to Contribute

- 🐛 **Bug Reports** - Help us identify and fix issues
- ✨ **Feature Requests** - Suggest new functionality
- 📝 **Documentation** - Improve guides and examples
- 💻 **Code Contributions** - Submit bug fixes and features
- 🧪 **Testing** - Help test new features and releases
- 🎨 **Design** - Improve UI/UX of the dashboard

## 🚀 Getting Started

### 1. Fork & Clone
```bash
# Fork the repository on GitHub
git clone https://github.com/your-username/whatsapp-medical-chatbot.git
cd whatsapp-medical-chatbot
```

### 2. Set Up Development Environment

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
```

#### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env.local
# Edit .env.local with your API endpoints
```

### 3. Create Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-description
```

## 📋 Development Guidelines

### Code Style

#### Backend (Python)
- Use **Black** for code formatting: `black .`
- Follow **PEP 8** style guidelines
- Add **type hints** for function parameters and returns
- Write **docstrings** for all functions and classes

```python
def process_medical_query(query: str, model: Any) -> Dict[str, Any]:
    """
    Process a medical query using the ML model.
    
    Args:
        query: User's medical question
        model: Trained ML model instance
        
    Returns:
        Dictionary containing response and metadata
    """
    # Implementation here
```

#### Frontend (TypeScript/React)
- Use **ESLint** and **Prettier** for formatting
- Follow **React best practices** and hooks patterns
- Use **TypeScript** for all new code
- Write **JSDoc comments** for complex functions

```typescript
/**
 * Hook for managing chatbot conversations
 * @param apiUrl - Backend API endpoint
 * @returns Conversation state and management functions
 */
export const useConversations = (apiUrl: string) => {
  // Implementation here
};
```

### Testing Requirements

#### Backend Tests
```bash
# Run tests
python -m pytest tests/

# Test coverage
python -m pytest --cov=. tests/

# Minimum 80% coverage required
```

#### Frontend Tests
```bash
# Unit tests
npm run test

# E2E tests
npm run test:e2e

# Coverage report
npm run test:coverage
```

### Commit Message Format

Use conventional commits format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(backend): add symptom severity classification
fix(frontend): resolve dashboard loading issue
docs(readme): update deployment instructions
```

## 🐛 Bug Reports

When reporting bugs, please include:

### Bug Report Template
```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**Environment:**
- OS: [e.g. macOS, Windows, Linux]
- Browser: [e.g. Chrome, Safari]
- Version: [e.g. 1.0.0]
- Backend URL: [if applicable]

**Additional context**
Any other context about the problem.
```

## ✨ Feature Requests

### Feature Request Template
```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Other solutions you've thought about.

**Additional context**
Screenshots, mockups, or examples.

**Implementation ideas**
If you have technical suggestions.
```

## 🔄 Pull Request Process

### 1. Before Submitting
- [ ] Code follows style guidelines
- [ ] Tests pass locally
- [ ] Documentation updated
- [ ] Self-review completed
- [ ] Related issues linked

### 2. Pull Request Template
```markdown
## Description
Brief description of changes.

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots of UI changes.

## Checklist
- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes (or clearly documented)
```

### 3. Review Process
1. **Automated Checks** - CI/CD pipeline runs tests
2. **Code Review** - Maintainer reviews code
3. **Testing** - Feature tested in staging environment
4. **Approval** - Changes approved by maintainer
5. **Merge** - PR merged to main branch

## 🏥 Medical Content Guidelines

### Safety First
- **Always include disclaimers** for medical advice
- **Encourage professional consultation** for serious symptoms
- **Avoid definitive diagnoses** - provide informational guidance only
- **Use evidence-based information** from reputable medical sources

### Content Standards
- **Accurate Information** - Verify medical facts
- **Clear Language** - Use simple, understandable terms
- **Cultural Sensitivity** - Consider diverse backgrounds
- **Accessibility** - Ensure content is accessible to all users

## 🧪 Testing Guidelines

### Backend Testing
```python
# Example test structure
def test_medical_query_processing():
    """Test medical query processing functionality."""
    query = "I have fever and headache"
    result = process_medical_query(query, mock_model)
    
    assert result['status'] == 'success'
    assert 'disclaimer' in result['response']
    assert len(result['response']) > 0
```

### Frontend Testing
```typescript
// Example component test
describe('ChatInterface', () => {
  it('should display medical disclaimer', () => {
    render(<ChatInterface />);
    expect(screen.getByText(/disclaimer/i)).toBeInTheDocument();
  });
});
```

## 📚 Documentation

### What to Document
- **New Features** - Usage examples and API changes
- **Configuration** - Environment variables and setup
- **Deployment** - Updated deployment instructions
- **Troubleshooting** - Common issues and solutions

### Documentation Style
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Update relevant README files

## 🌍 Internationalization

If contributing translations:
- Use proper locale codes (e.g., `en-US`, `es-ES`)
- Maintain consistent terminology
- Consider cultural context for medical terms
- Test with right-to-left languages if applicable

## 🔒 Security Considerations

### Sensitive Data
- **Never commit credentials** or API keys
- **Use environment variables** for configuration
- **Sanitize user inputs** to prevent injection attacks
- **Follow OWASP guidelines** for web security

### Medical Data Privacy
- **Comply with HIPAA** and local privacy laws
- **Minimize data collection** - only collect necessary information
- **Secure data transmission** - use HTTPS everywhere
- **Implement proper logging** without exposing sensitive data

## 🎯 Priority Areas

We especially welcome contributions in these areas:

### High Priority
- 🐛 **Bug fixes** for existing functionality
- 📱 **Mobile responsiveness** improvements
- 🔒 **Security enhancements**
- 📊 **Performance optimizations**

### Medium Priority
- ✨ **New medical knowledge** integration
- 🌐 **Multi-language support**
- 📈 **Advanced analytics** features
- 🎨 **UI/UX improvements**

### Future Features
- 🎤 **Voice message support**
- 📅 **Appointment booking** integration
- 🏥 **Telemedicine** features
- 🤖 **Advanced AI models**

## 🏆 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page
- **Special mentions** in project updates

## 📞 Getting Help

### Community Support
- 💬 **GitHub Discussions** - Ask questions and share ideas
- 🐛 **GitHub Issues** - Report bugs and request features
- 📧 **Email** - [maintainer-email@example.com] for sensitive issues

### Development Help
- 📖 **Documentation** - Check existing guides first
- 🔍 **Code Search** - Look for similar implementations
- 🧪 **Tests** - Run existing tests to understand expected behavior

## 📜 Code of Conduct

### Our Pledge
We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Expected Behavior
- **Be respectful** and inclusive
- **Be collaborative** and constructive
- **Be patient** with newcomers
- **Focus on the project** goals

### Unacceptable Behavior
- Harassment or discrimination
- Trolling or insulting comments
- Personal attacks
- Publishing private information

## 📄 License

By contributing, you agree that your contributions will be licensed under the same MIT License that covers the project.

---

**Thank you for contributing to accessible healthcare technology! 🏥❤️**