// hello_algolia.js
import algoliasearch from "algoliasearch";

export function search_engine(search_text: string) {
  // Connect and authenticate with your Algolia app
  const add_client = algoliasearch(
    "5JQ98FK7KJ",
    "69e0f0d5c62f30afa587322210d3b89a"
  );
  // Create a new index and add a record

  const index = add_client.initIndex("decath-index");
  // const objects = [
  //   {
  //     firstname: "Jimmie",
  //     lastname: "Barninger",
  //     objectID: "myID1",
  //   },
  //   {
  //     firstname: "Warren",
  //     lastname: "Speach",
  //     objectID: "myID2",
  //   },
  // ];
  // console.log("before save");
  // index.saveObjects(objects).then(({ objectIDs }) => {
  //   console.log(objectIDs);
  // });
  // console.log("after save");

  // Search the index and print the results
  console.log("search text", search_text);
  return index.search(search_text).then(({ hits }) => hits);
}

export function algolia_insert(objects: any) {
  const add_client = algoliasearch(
    "5JQ98FK7KJ",
    "69e0f0d5c62f30afa587322210d3b89a"
  );

  const index = add_client.initIndex("decath-index");
  // const objects = [
  //   {
  //     firstname: "Jimmie",
  //     lastname: "Barninger",
  //     objectID: "myID1",
  //   },
  //   {
  //     firstname: "Warren",
  //     lastname: "Speach",
  //     objectID: "myID2",
  //   },
  // ];
  objects = objects.map((data: any)=> {
    return {...data, objectID:data.id}
  })
  // console.log(result)
  index.saveObjects(objects).then(({ objectIDs }) => {
    console.log(objectIDs);
  });
}
