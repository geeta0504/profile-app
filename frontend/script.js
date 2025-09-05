const profilesList = document.getElementById('profilesList');
const projectsList = document.getElementById('projectsList');

const API_BASE = 'http://127.0.0.1:8000/api'; // Make sure backend is running

async function loadProfiles() {
  const res = await fetch(`${API_BASE}/profiles/`);
  const profiles = await res.json();
  profilesList.innerHTML = '';
  profiles.forEach(p => {
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `
      <h3>${p.name}</h3>
      <p><strong>Email:</strong> ${p.email}</p>
      <p><strong>Education:</strong> ${p.education || '-'}</p>
      <p><strong>Skills:</strong> ${p.skills}</p>
      <p><strong>Bio:</strong> ${p.bio || '-'}</p>
      <p><strong>Work:</strong> ${
        p.work.length ? p.work.map(w => `<a href="${w.links.portfolio || '#'}">${w.company}</a>`).join(', ') : '-'
      }</p>
      <p><strong>Projects:</strong> ${
        p.projects.length ? p.projects.map(pr => `<a href="${pr.links.portfolio || '#'}">${pr.title}</a>`).join(', ') : '-'
      }</p>
    `;
    profilesList.appendChild(div);
  });
}

async function loadProjects() {
  const res = await fetch(`${API_BASE}/projects/`);
  const projects = await res.json();
  projectsList.innerHTML = '';
  projects.forEach(p => {
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `
      <h3>${p.title}</h3>
      <p><strong>Technologies:</strong> ${p.technologies}</p>
      <p>${p.description}</p>
      <p><a href="${p.links.portfolio || '#'}">Portfolio</a> | <a href="${p.links.github || '#'}">GitHub</a></p>
    `;
    projectsList.appendChild(div);
  });
}

async function searchBySkill() {
  const skill = document.getElementById('skillInput').value;
  if(!skill) {
    loadProjects();
    return;
  }
  const res = await fetch(`${API_BASE}/projects-by-skill/?skill=${skill}`);
  const projects = await res.json();
  projectsList.innerHTML = '';
  projects.forEach(p => {
    const div = document.createElement('div');
    div.className = 'card';
    div.innerHTML = `
      <h3>${p.title}</h3>
      <p><strong>Technologies:</strong> ${p.technologies}</p>
      <p>${p.description}</p>
      <p><a href="${p.links.portfolio || '#'}">Portfolio</a> | <a href="${p.links.github || '#'}">GitHub</a></p>
    `;
    projectsList.appendChild(div);
  });
}



const skillsList = document.getElementById('skillsList');

async function loadTopSkills() {
  const res = await fetch(`${API_BASE}/skills/top/`);
  const data = await res.json();
  skillsList.innerHTML = '';
  data.top_skills.forEach(([skill, count]) => {
    const li = document.createElement('li');
    li.textContent = `${skill} (${count})`;
    skillsList.appendChild(li);
  });
}

// Load everything on page load
loadProfiles();
loadTopSkills();
loadProjects();
