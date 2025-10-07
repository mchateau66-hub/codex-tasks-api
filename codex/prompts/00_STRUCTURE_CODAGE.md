# 📁 00_STRUCTURE_CODAGE.md  
### Structure du projet — Étape 0  

Ce document définit la structure initiale du projet **codage-informatique**,  
destiné à être ouvert et exploité dans **Cursor** avec le **Codex IA**.

---

## 🧩 Arborescence du projet
codage-informatique/
├── codex/
│ ├── INDEX.md
│ ├── prompts/
│ │ ├── system.md
│ │ └── repo-context.md
│ ├── standards/
│ │ ├── algorithmique.md
│ │ ├── designing-data-intensive.md
│ │ ├── python-optimisation.md
│ │ ├── building-microservices.md
│ │ └── ai-assisted-coding.md
│ ├── stacks/
│ │ ├── python/
│ │ │ ├── style-pep8.md
│ │ │ └── tooling.md
│ │ ├── nodejs/
│ │ │ ├── style.md
│ │ │ └── tooling.md
│ ├── templates/
│ │ ├── SPEC_MODULE.md
│ │ ├── ADR.md
│ │ ├── TEST_PLAN.md
│ │ └── PR_TEMPLATE.md
│ └── checklists/
│ ├── pre-commit.md
│ ├── security.md
│ └── release.md
│
├── src/
│ ├── main.py
│ └── init.py
│
├── tests/
│ └── test_main.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── notes.md

---

## 🧠 Description rapide

| Élément | Description |
|----------|-------------|
| **`codex/`** | Référentiel de toutes les règles, ouvrages et prompts. |
| **`codex/prompts/system.md`** | Prompt IA principal — gère la qualité, les tests, la sécurité. |
| **`codex/prompts/repo-context.md`** | Contexte technique du projet (stack, outils, conventions). |
| **`codex/standards/`** | Résumés de livres et normes (Clean Code, OWASP, etc.). |
| **`codex/stacks/`** | Règles spécifiques selon le langage utilisé. |
| **`codex/templates/`** | Modèles de documents (SPEC, ADR, PR template, test plan). |
| **`codex/checklists/`** | Contrôles qualité avant commit, release, sécurité. |
| **`src/`** | Code source de ton projet. |
| **`tests/`** | Ensemble des tests unitaires et d’intégration. |
| **`README.md`** | Présentation générale du projet. |
| **`requirements.txt`** | Dépendances Python. |
| **`notes.md`** | Notes, documentation complémentaire ou historique. |

---

## 🧰 Étapes d’utilisation dans Cursor

1. **Créer le dossier** `codage-informatique` sur ton ordinateur.  
2. **Y coller cette structure** (avec ce fichier `00_STRUCTURE_CODAGE.md`).  
3. **Ouvrir Cursor** → “Open Project” → sélectionner `codage-informatique/`.  
4. **Créer les fichiers suivants :**
   - `codex/prompts/system.md`
   - `codex/prompts/repo-context.md`
   - `codex/INDEX.md`
5. **Lancer une session Chat** :
   - Copier le contenu de `system.md` dans la fenêtre de chat.  
   - Ajouter la commande :  
     > “Lis le repo-context et crée un module Python `users` avec endpoints CRUD, tests et CI.”  

---

## ✅ Résultat attendu
Une arborescence complète lisible par Cursor et un environnement prêt pour :
- la génération automatisée de code conforme à ton Codex,
- la création de modules Python/Node,
- la gestion des tests, documentation et sécurité intégrée.

---

🧠 **Conseil :**  
Tu peux déposer ce fichier à la racine de ton projet pour qu’il serve de *guide permanent* dans ton environnement Cursor.
