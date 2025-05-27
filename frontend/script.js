fetch('data.json')
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('suggestions');
    
    data.forEach(item => {
      const div = document.createElement('div');
      div.className = 'suggestion-card';

      const binIcons = {
        organic: '<i class="fas fa-leaf"></i>',
        plastic: '<i class="fas fa-bottle-water"></i>',
        metal: '<i class="fas fa-cogs"></i>'
      };

      const typesHTML = item.suggested_bin_types.map(type =>
        `<span>${binIcons[type.toLowerCase()] || ''} ${type}</span>`
      ).join(', ');

      div.innerHTML = `
        <h2>${item.street}</h2>
        <p><i class="fas fa-dumpster"></i> <strong>Predicted Bins:</strong> ${item.predicted_bin_count}</p>
        <p><i class="fas fa-trash"></i> <strong>Types:</strong> ${typesHTML}</p>
        <p><i class="fas fa-map-marker-alt"></i> <strong>Location:</strong> (${item.suggested_location.latitude}, ${item.suggested_location.longitude})</p>
      `;

      container.appendChild(div);
    });
  })
  .catch(error => {
    console.error('Error loading data:', error);
  });

