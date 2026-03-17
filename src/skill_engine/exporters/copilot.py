def export_skill_to_copilot(skill):
    return {'id': skill.id, 'version': skill.version, 'title': skill.title, 'purpose': skill.purpose, 'compatibility': ['copilot'], 'source_architecture': 'andyai-skill-engine'}
