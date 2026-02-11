const ProjectCard = ({ title, desc }) => (
  <div className="project">
    <h3>{title}</h3>
    <p>{desc}</p>
    <button>View</button>
  </div>
);

const Projects = () => {
  return (
    <section id="projects">
      <h2>Projects</h2>

      <div className="project-grid">
        <ProjectCard
          title="Online Electronics Shop"
          desc="Full-stack e-commerce app using React & MongoDB"
        />

        <ProjectCard
          title="Attendance Management System"
          desc="Student & company attendance tracking platform"
        />
      </div>
    </section>
  );
};

export default Projects;
