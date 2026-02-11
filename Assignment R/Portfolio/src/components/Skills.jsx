const Skill = ({ name }) => <span className="skill">{name}</span>;

const Skills = () => {
  const skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Git",
    "MongoDB",
    "Node.js"
  ];

  return (
    <section id="skills" className="card">
      <h2>Skills</h2>
      <div className="skills-wrap">
        {skills.map((skill, i) => (
          <Skill key={i} name={skill} />
        ))}
      </div>
    </section>
  );
};

export default Skills;
