use std::fs;

fn get_file_data(path: &str) -> Vec<(String, Vec<u32>)> {
    let file_contents = fs::read_to_string(path).expect("Couldn't read file!");
    let mut springs: Vec<(String, Vec<u32>)> = Vec::new();

    let mut file_lines = file_contents.lines();

    while let Some(line) = file_lines.next() {
        let split_line = Vec::from_iter(line.split(" "));
        springs.push((split_line[0].to_string(), Vec::from_iter(split_line[1].split(",").map(|c| c.parse::<u32>().unwrap()))));
    }
    return springs;
}

fn count_possible_configs(spring_string: String, broken_groups: Vec<u32>) -> u32 {
    let broken_segments = spring_string.split(".").filter(|sub| sub.contains("?"));

    
    return 1;
}

fn main() {
    let springs = get_file_data("./input.txt");
}
