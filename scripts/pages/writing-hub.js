var items = [
  ['writing.html', 'IELTS Writing Checker', 'Write an essay or letter and check word count, linking words and structure.'],
  ['writing-models.html', 'IELTS Writing Models', 'Task 1 and Task 2 model answers with charts, letters and notes.'],
  ['writing-band9.html', 'Writing Band 9', 'Task 2 essay types, annotated Band 9 targets, skills lessons and drills.']
];
app.innerHTML = back('index.html#geography-hub/study', 'Back to Train Your Brain') + head('IELTS Writing') +
  '<div class="wm-grid">' + items.map(function(t){ return '<a class="wm-tile" href="' + t[0] + '"><b>' + esc(t[1]) + '</b><span class="wm-w">' + esc(t[2]) + '</span></a>'; }).join('') + '</div>';
