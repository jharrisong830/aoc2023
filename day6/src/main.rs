use std::{
    fs,
    collections::HashMap
};

/**
 * Parses the input file and returns two representations of the data (hashmap for pt1, tuple of full time/dist values for part 2)
 */
fn get_file_data(path: &str) -> (HashMap<u64, u64>, (u64, u64)) {
    let mut dict: HashMap<u64, u64> = HashMap::new();

    let file_contents = fs::read_to_string(path).expect("Couldn't read file!");

    let mut file_lines = file_contents.lines();

    let times = file_lines.next();
    let distances = file_lines.next();

    match (times, distances) {
        (Some(tm), Some(dst)) => {
            let time_data = Vec::from_iter(tm.split_whitespace());
            let dist_data = Vec::from_iter(dst.split_whitespace());
            for i in 1..time_data.len() {
                dict.insert(time_data[i].parse::<u64>().unwrap(), dist_data[i].parse::<u64>().unwrap());
            }
            return (dict, (time_data[1..].join("").parse::<u64>().unwrap(), dist_data[1..].join("").parse::<u64>().unwrap())) 
        },
        _ => panic!("Invalid file contents!")
    }
}



fn num_options_for_race(time: u64, dist: u64) -> usize {
    let options: Vec<u64> = (1..time).filter(|speed| speed * (time - speed) > dist).collect();
    return options.len()
}



fn main() {
    let (time_dist_map, (total_time, total_dist)) = get_file_data("./input.txt");
    let options_per_race = time_dist_map.keys().map(|k| num_options_for_race(*k, *time_dist_map.get(k).unwrap()));
    let part1_ans = options_per_race.fold(1, |x, y| x * y);
    println!("Part 1 answer: {}", part1_ans);

    let part2_ans = num_options_for_race(total_time, total_dist);
    println!("Part 2 answer: {}", part2_ans);
}
