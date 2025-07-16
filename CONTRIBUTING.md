# Contribution Guidelines

Contributions to the Kiijs library are welcome. As a contributor, here are the guidelines we would like you to follow:

- [Code of Conduct](#coc)
- [Question or Problem?](#question)
- [Issues and Bugs](#issue)
- [Feature Requests](#feature)
- [Submission Guidelines](#submit)
- [Coding Rules](#rules)
- [Commit Message Guidelines](#commit)

## <a name="coc"></a> Code of Conduct

Please read and follow our [Code of Conduct][coc].

## <a name="issue"></a> Found a Bug?

If you find a bug in the source code [submit a bug report issue](#submit-issue).
Even better, you can [submit a Pull Request](#submit-pr) with a fix.

## <a name="feature"></a> Missing a Feature?

You can *request* a new feature by [submitting a feature request issue](#submit-issue).
If you would like to *implement* a new feature:

- For a **Major Feature**, first [open an issue](#submit-issue) and outline your proposal so that it can be discussed.
- **Small Features** can be crafted and directly [submitted as a Pull Request](#submit-pr).

## <a name="submit"></a> Submission Guidelines

### <a name="submit-issue"></a> Submitting an Issue

Before you submit an issue, please search the [issue tracker][issues]. An issue for your problem might already exist and the discussion might inform you of workarounds readily available.

For bug reports, it is important that we can reproduce and confirm it. For this, we need you to provide a minimal reproduction instruction (this is part of the bug report issue template).

You can file new issues by selecting from our [new issue templates][new-issue] and filling out the issue template.

### <a name="submit-pr"></a> Submitting a Pull Request (PR)

Before you submit your Pull Request (PR) consider the following guidelines:

1. All Pull Requests should be based off of and opened against the `main` branch.

2. Search [Existing PRs][prs] for an open or closed PR that relates to your submission.
   You don't want to duplicate existing efforts.

3. Be sure that an issue exists describing the problem you're fixing, or the design for the feature you'd like to add.

4. [Fork](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) the [repository][github].

5. In your forked repository, make your changes in a new git branch created off of the `main` branch.

6. Make your changes, **including test cases and documentation updates where appropriate**.

7. Follow our [coding rules](#rules).

8. Run all tests and checks locally, as described in the [development guide][developing], and ensure they pass. This saves CI hours and ensures you only commit clean code.

9. Commit your changes using a descriptive commit message that follows our [commit message conventions](#commit).

10. Push your branch to GitHub.

11. In GitHub, send a pull request to `KiiBlockchain:main`.

#### Reviewing a Pull Request

The Kiijs team reserves the right not to accept pull requests from community members who haven't been good citizens of the community. Such behavior includes not following our [code of conduct][coc] and applies within or outside the managed channels.

When you contribute a new feature, the maintenance burden is transferred to the core team. This means that the benefit of the contribution must be compared against the cost of maintaining the feature.

#### Addressing review feedback

If we ask for changes via code reviews then:

1. Make the required updates to the code.

2. Re-run the tests and checks to ensure they are still passing.

3. Create a new commit and push to your GitHub repository (this will update your Pull Request).

#### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes from the (upstream) repository.

## <a name="rules"></a> Coding Rules

To ensure consistency throughout the source code, keep these rules in mind as you are working:

- All code must pass our code quality checks (linters, formatters, etc).
- All features **must be tested** via unit-tests and if applicable integration-tests. Bug fixes also require tests, because the presence of bugs usually indicates insufficient test coverage. Tests help to: 

    1. Prove that your code works correctly, and
    2. Guard against future breaking changes and lower the maintenance cost. 

- All public features **must be documented**.
- All files must include a license header. 
- Keep API compatibility in mind when you change any code under `Kiijs`. Above version `1.0.0`, breaking changes can happen across versions with different left digit. Below version `1.0.0`, they can happen across versions with different middle digit. Reviewers of your pull request will comment on any API compatibility issues.

## <a name="commit"></a> Commit Message Convention

Please follow the [Conventional Commits v1.0.0][convcommit]. The commit types must be one of the following:

- **build**: Changes that affect the build system or external dependencies
- **ci**: Changes to our CI configuration files and scripts
- **docs**: Changes to the documentation
- **feat**: A new feature
- **fix**: A bug fix
- **nfunc**: Code that improves some non-functional characteristic, such as performance, security, ...
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests or correcting existing tests

[coc]: ./CODE_OF_CONDUCT.md
[issues]: https://github.com/KiiChain/kiijs-sdk/issues
[new-issue]: https://github.com/KiiChain/kiijs-sdk/issues/new/choose
[prs]: https://github.com/KiiChain/kiijs-sdk/pulls
[convcommit]: https://www.conventionalcommits.org/en/v1.0.0/
[github]: https://github.com/KiiChain/kiijs-sdk

## <a name="docs"></a> Documentation Guidelines

### Documentation Structure and Organization

Our documentation follows GitBook structure with a clear hierarchy designed to provide comprehensive coverage of all aspects of the KiiChain ecosystem:

**Directory Structure:**
- `/docs/getting-started/` - Onboarding guides, installation instructions, and basic setup procedures
- `/docs/guides/` - Step-by-step tutorials, how-to guides, and practical walkthroughs
- `/docs/reference/` - API documentation, technical specifications, and comprehensive reference materials
- `/docs/examples/` - Code examples, use cases, implementation samples, and practical demonstrations
- `/docs/troubleshooting/` - Common issues, error resolution guides, and debugging information
- `/docs/advanced/` - Advanced topics, optimization guides, and expert-level content

**File Naming Conventions:**
- Use lowercase with hyphens for readability: `getting-started.md`, `node-validator-setup.md`
- Be descriptive and specific: `node-validator-setup.md` instead of generic `setup.md`
- Group related files in appropriate subdirectories for logical organization
- Use `README.md` files for directory overviews and navigation guidance
- Always update `SUMMARY.md` for proper navigation structure and GitBook integration

### Writing Style Guide

**Tone and Voice:**
- **Clear and Professional**: Use straightforward, accessible language that serves both technical and non-technical users effectively
- **Active Voice Preferred**: Write "Deploy the contract" instead of "The contract should be deployed"
- **Concise Communication**: Keep sentences under 20 words when possible for maximum clarity and readability
- **Consistent Terminology**: Use the same terms throughout all documentation to avoid confusion
- **Inclusive Language**: Use "you" instead of "he/she", avoid unexplained jargon, and ensure accessibility

**Content Structure Best Practices:**
- **Start with Overview**: Provide a brief summary of what the document covers and learning objectives
- **Prerequisites Section**: List required knowledge, tools, and setup requirements before starting
- **Step-by-Step Instructions**: Number complex procedures clearly and provide logical progression
- **Code Examples**: Include practical, tested examples with expected outputs and explanations
- **Expected Outcomes**: Describe what users should see, experience, or achieve at each step
- **Next Steps**: Link to related documentation and suggest follow-up actions or advanced topics

**Technical Writing Standards:**
- **Code Examples**: Always test before publishing, include expected outputs, and provide context
- **Screenshots and Visuals**: Include when helpful, use consistent styling, annotations, and high-quality images
- **Link Guidelines**: Use descriptive text, avoid "click here" or generic phrases, test all links regularly
- **Warnings and Notes**: Use callout boxes, consistent formatting for important information and alerts
- **Version Information**: Specify software versions, compatibility requirements, and update dates when relevant

### Local Development and Preview Setup

**Prerequisites:**
- Node.js 14.x or higher installed on your system
- npm or yarn package manager for dependency management
- Git installed and configured with your GitHub credentials
- Text editor or IDE for markdown editing

**Initial Setup Process:**
1. Clone your forked repository to your local machine:
   ```bash
   git clone https://github.com/YOUR_USERNAME/kiichain-docs.git
   cd kiichain-docs
   ```

2. Install GitBook CLI globally for documentation building:
   ```bash
   npm install -g gitbook-cli
   ```

3. Install project dependencies and GitBook plugins:
   ```bash
   gitbook install
   ```

4. Start the development server for live preview:
   ```bash
   gitbook serve
   ```

5. Open your browser to `http://localhost:4000` to view the documentation

**Development Workflow:**
1. Create a feature branch for your changes: `git checkout -b docs/your-feature-name`
2. Make your documentation changes using your preferred editor
3. Preview changes locally using `gitbook serve` and verify formatting
4. Test all links, code examples, and interactive elements thoroughly
5. Commit changes with descriptive, conventional commit messages
6. Push your branch to your fork and create a pull request

### Markdown Best Practices and Standards

**Heading Hierarchy:**
```markdown
# Page Title (H1) - Only one per document, used for main page title
## Major Section (H2) - Primary content divisions
### Subsection (H3) - Secondary content divisions
#### Details (H4) - Use sparingly, only for granular details
```

**Code Block Formatting:**
Always specify language for proper syntax highlighting and better readability:
```bash
kii tx bank send alice bob 1000ukii --chain-id kiichain-testnet --gas auto
```

```javascript
const client = new KiiChainClient({
  chainId: 'kiichain-testnet',
  rpcEndpoint: 'https://rpc.kiichain.io'
});
```

**Lists and Structure:**
- Use consistent bullet points and numbering throughout documents
- Maintain proper indentation (two spaces for sub-items) for hierarchy
- Number complex procedures for clarity and easy reference
- Use task lists for checklists and progress tracking: `- [x] Completed task`
- Group related items logically and use parallel structure

**Links and Media:**
- Use descriptive link text that explains the destination
- Test all links before submitting and regularly during reviews
- Include meaningful alt text for images: `![KiiChain network architecture diagram](image.png)`
- Use relative links for internal documentation to maintain portability
- Optimize images for web use and consistent display across devices

**Tables:**
Use proper markdown table formatting with clear headers and aligned columns:
```markdown
| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| address   | string | Yes | Wallet address | kii1abc... |
| amount    | number | Yes | Amount in ukii | 1000000 |
| memo      | string | No | Optional memo | "Payment" |
```

### Documentation Review Process

**Before Submitting:**
1. **Content Review**: Verify all information is accurate, up-to-date, and technically correct
2. **Link Testing**: Test all internal and external links to ensure they work properly
3. **Code Verification**: Run all code examples to ensure they work as documented
4. **Grammar Check**: Use spell-check and grammar tools for professional quality
5. **Consistency Review**: Ensure consistency with existing documentation style and terminology
6. **Navigation Update**: Update `SUMMARY.md` if you've added new pages or sections

**Pull Request Guidelines:**
- **Title**: Use clear, descriptive titles that explain the change (e.g., "Add validator setup guide")
- **Description**: Explain what was added, changed, or fixed and provide context for the changes
- **Screenshots**: Include before/after screenshots for UI changes or visual improvements
- **Testing**: Describe how changes were tested and verified
- **Related Issues**: Link to relevant GitHub issues using "Fixes #123" or "Closes #456"

**Review Process:**
1. **Documentation Team Review**: Reviews for accuracy, clarity, and adherence to style guidelines
2. **Technical Team Review**: Validates technical correctness and implementation details
3. **Community Feedback**: Incorporates feedback from community members and users
4. **Final Approval**: Final review and merge after all requirements are met

### Common Documentation Patterns

**Tutorial Structure:**
1. **Introduction**: Clearly explain what will be accomplished and why it's important
2. **Prerequisites**: List required knowledge, tools, accounts, and setup requirements
3. **Step-by-Step Instructions**: Provide numbered, detailed steps with expected outcomes
4. **Verification**: Explain how to confirm success and validate the implementation
5. **Troubleshooting**: Address common issues, error messages, and resolution steps
6. **Next Steps**: Suggest follow-up actions, advanced topics, or related documentation

**API Documentation:**
- **Endpoint Overview**: Clear description of purpose and functionality
- **Request/Response Examples**: Complete examples in multiple formats (JSON, curl, SDK)
- **Parameter Tables**: Detailed parameter descriptions with types, requirements, and examples
- **Error Codes**: Comprehensive error handling with codes, messages, and solutions
- **SDK Examples**: Implementation examples in multiple programming languages

**Configuration Guide:**
- **Default Configuration**: Show default settings with explanations
- **Parameter Descriptions**: Detailed explanation of each configuration option
- **Environment-Specific Settings**: Different configurations for development, staging, production
- **Security Considerations**: Best practices for secure configuration
- **Performance Optimization**: Tips for optimizing performance through configuration

### Resources and Tools

**Helpful Documentation Tools:**
- [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) - For creating complex tables
- [GitBook Documentation](https://docs.gitbook.com/) - Official GitBook documentation and best practices
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) - Quick reference guide
- [Hemingway Editor](https://hemingwayapp.com/) - For improving readability and clarity

**Style Guides and References:**
- [Google Developer Documentation Style Guide](https://developers.google.com/style) - Comprehensive writing guidelines
- [Microsoft Writing Style Guide](https://docs.microsoft.com/en-us/style-guide/welcome/) - Professional writing standards
- [GitBook Best Practices](https://docs.gitbook.com/getting-started/overview) - Platform-specific guidelines

**Quality Assurance:**
- Use automated link checkers for large documentation sets
- Implement consistent formatting through markdown linters
- Regular review cycles for keeping content current and accurate
- User feedback integration for continuous improvement

For questions about documentation standards, major structural changes, or clarification on these guidelines, please open an issue to discuss with the documentation team before starting work. This ensures alignment with project goals and prevents duplicate efforts.
