"""Uses set operations to analyze shared and unique skills across teams."""

TEAM_ALPHA = {"python", "sql", "docker"}
TEAM_BETA = {"python", "go", "kubernetes"}

if __name__ == "__main__":
    shared = TEAM_ALPHA & TEAM_BETA
    unique_alpha = TEAM_ALPHA - TEAM_BETA
    unique_beta = TEAM_BETA - TEAM_ALPHA
    all_skills = TEAM_ALPHA | TEAM_BETA

    print("Shared skills:", shared)
    print("Unique to alpha:", unique_alpha)
    print("Unique to beta:", unique_beta)
    print("All skills:", all_skills)
