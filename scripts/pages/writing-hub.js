var items = [
  ['writing.html', 'IELTS Writing Checker'],
  ['writing-models.html', 'IELTS Writing Models'],
  ['writing-band9.html', 'Writing Band 9']
];
app.innerHTML = back('index.html#geography-hub/study', 'Back to Train Your Brain') + head('IELTS Writing') +
  '<div class="sport-hub-grid">' + items.map(function(t, i){ return '<a class="sport-hub-tile" href="' + t[0] + '"' + (i === 2 ? ' style="grid-column:1 / -1;"' : '') + '><span class="name">' + esc(t[1]) + '</span></a>'; }).join('') + '</div>';
