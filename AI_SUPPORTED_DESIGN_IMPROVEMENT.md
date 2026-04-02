# AI-Supported Design Improvement (Compulsory)

## 1. AI Evaluation Context

- **AI tool used:** ChatGPT (OpenAI)
- **Prototype evaluated:** Django wireframe for CivicFix SA (`/` dashboard and `/reports/new/` report form)
- **Target users from Part A:** Community residents reporting municipal service issues
- **Problem from Part A:** Residents need a simple, visible, and reliable way to submit and track local issues
- **Conceptual model alignment from Part B:** User-centered reporting flow:
  1. Open dashboard
  2. Start report
  3. Provide category + location + evidence
  4. Submit and monitor status

## 2. AI Feedback Received

The AI identified the following usability and UX issues in the original wireframe:

1. **Navigation feedback was weak**
   - Users could not easily tell which page was active.
2. **Quick Access labels were inconsistent with destination behavior**
   - Buttons like `Profile` and `Settings` pointed to the report form, which could confuse users.
3. **Form guidance was minimal**
   - Required vs optional fields were not explicit.
4. **Input feedback was insufficient**
   - Weak visual cues for invalid input and keyboard focus.
5. **Affordance could be improved**
   - Clickable elements needed stronger hover/focus responses.

## 3. Changes Made to the Design

Based on the AI feedback, the following improvements were implemented:

1. **Active navigation state added**
   - Dashboard and Report Issue links now show active state on the current page.
2. **Navigation/link feedback improved**
   - Hover and focus styling added for nav links, CTA buttons, and quick-access actions.
3. **Quick Access wording refined**
   - Updated labels to clearer task-oriented wording (`Report New Issue`, `Track Existing`, `Help Center`).
4. **Form clarity improved**
   - Added `*` markers for required fields and helper copy: `Fields marked with * are required.`
5. **Field-level guidance added**
   - Added hints under issue type, photo, and location fields.
6. **Input feedback strengthened**
   - Added clear focus outlines and invalid input border styling.

## 4. Accepted and Rejected Suggestions

### Accepted Suggestions

1. **Add active page state in navigation**
   - **Decision:** Accepted
   - **Justification:** Supports visibility and orientation; users always know where they are.
2. **Improve hover/focus feedback**
   - **Decision:** Accepted
   - **Justification:** Reinforces affordance and accessibility for mouse and keyboard users.
3. **Clarify form requirements and hints**
   - **Decision:** Accepted
   - **Justification:** Reduces user uncertainty and potential input mistakes.
4. **Rename quick actions for task clarity**
   - **Decision:** Accepted
   - **Justification:** Better reflects user goals in the conceptual reporting flow.

### Rejected Suggestions

1. **Implement full account management pages now (Profile/Settings/Help)**
   - **Decision:** Rejected for this iteration
   - **Justification:** Out of scope for the current assignment requirement (basic wireframe structure).
2. **Integrate live map/geolocation API in this prototype**
   - **Decision:** Rejected for this iteration
   - **Justification:** Adds technical complexity beyond current wireframe objectives; placeholder guidance is sufficient for now.

## 5. Iterative Outcome

The updated prototype demonstrates an iterative design process:

- Started with the original Django wireframe
- Used AI to identify concrete usability issues
- Applied focused design improvements
- Kept changes aligned to the community-reporting conceptual model, user needs, and assignment scope

This iteration improves **visibility**, **feedback**, **consistency**, and **affordance** while preserving the required two-app Django structure.
