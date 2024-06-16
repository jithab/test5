let books = [
  {
    country: "USA",
    weight: 5 * 5,
    chapters: [
      {
        name: "The New York Times",
        url: "https://www.nytimes.com/international/",
        weight: 5,
      },
      {
        name: "Obituaries",
        url: "https://www.nytimes.com/international/section/obituaries",
        weight: 5,
      },
    ],
  },
  {
    country: "UK",
    weight: 5 * 5,
    chapters: [
      {
        name: "The Guardian",
        url: "https://www.theguardian.com/international/",
        weight: 5,
      },
      {
        name: "Comment is Free",
        url: "https://www.theguardian.com/uk/commentisfree",
        weight: 4,
      },
      {
        name: "Tech",
        url: "https://www.theguardian.com/uk/technology",
        weight: 3,
      },
    ],
  },
  {
    country: "USA",
    weight: 5 * 5,
    chapters: [
      {
        name: "The Washington Post",
        url: "https://www.washingtonpost.com/world/",
        weight: 5,
      },
      {
        name: "Tech",
        url: "https://www.washingtonpost.com/business/technology/",
        weight: 4,
      },
      {
        name: "Opinions",
        url: "https://www.washingtonpost.com/opinions/",
        weight: 3,
      },
    ],
  },
  {
    country: "USA",
    weight: 3 * 5,
    chapters: [
      {
        name: "The Atlantic",
        url: "https://www.theatlantic.com/world/",
        weight: 5,
      },
    ],
  },
  {
    country: "USA",
    weight: 3 * 5,
    chapters: [
      {
        name: "The New Yorker",
        url: "https://www.newyorker.com/",
        weight: 5,
      },
    ],
  },
  {
    country: "USA",
    weight: 3 * 3,
    chapters: [
      {
        name: "Los Angeles Times",
        url: "https://www.latimes.com/",
        weight: 1,
      },
      {
        name: "Obituaries",
        url: "https://www.latimes.com/obituaries/",
        weight: 5,
      },
    ],
  },
];

let processedList = [];

function getTotalWeight(items) {
  let ret = 0;
  items.forEach(function (item, index) {
    ret += item.weight;
  });
  return ret;
}

function processList() {
  let booksWeight = getTotalWeight(books);
  console.log("Total Weight: " + booksWeight);
  let booksWeightStart = 0;
  books.forEach(function (book, index) {
    let chaptersWeight = getTotalWeight(book.chapters);

    let chaptersWeightSoFar = 0;
    book.chapters.forEach(function (chapter, chapterNumber) {
      chaptersWeightSoFar += chapter.weight;
      console.log("Name " + chapter.name);

      //console.log("1 Start: " + booksWeightStart + ", Weight: " + booksWeight);
      //console.log("2 Start: " + bookWeightSoFar + ", Weight: " + bookWeight);

      let name = book.chapters[0].name;
      if (chapterNumber > 0) name += " > " + book.chapters[chapterNumber].name;
      let endRange =
        (booksWeightStart +
          (book.weight * chaptersWeightSoFar) / chaptersWeight) /
        booksWeight;
      processedList.push({
        name: name,
        endRange: endRange,
        url: chapter.url,
        target: book.chapters[0].name,
      });
    });
    booksWeightStart += book.weight;
  });
}
function shuffleArray(array) {
  // Create a copy of the array to avoid modifying the original array
  let shuffledArray = array.slice();

  for (let i = shuffledArray.length - 1; i > 0; i--) {
    // Generate a random index between 0 and i
    const j = Math.floor(Math.random() * (i + 1));

    // Swap elements at indices i and j
    [shuffledArray[i], shuffledArray[j]] = [shuffledArray[j], shuffledArray[i]];
  }

  return shuffledArray;
}
processList();
let ul = document.getElementById("list");
let shuffled = shuffleArray(processedList);
shuffled.forEach(function (item, index) {
  let aTag = document.createElement("a");
  aTag.setAttribute("href", item.url);
  aTag.setAttribute("target", item.target);
  aTag.innerText = item.name;
  let li = document.createElement("li");
  li.appendChild(aTag);
  ul.appendChild(li);
});
