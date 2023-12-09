use std::{
    fs, 
    collections::HashMap
};

#[derive(Debug)]
struct Directions {
    left: String,
    right: String
}


fn get_file_data(path: &str) -> (Vec<char>, HashMap<String, Directions>) {
    let mut node_directions_map: HashMap<String, Directions> = HashMap::new();

    let file_contents = fs::read_to_string(path).expect("Couldn't read file!");

    let mut file_lines = file_contents.lines();

    let directions = String::from(file_lines.next().unwrap()); // L/R directions from the first line

    while let Some(line) = file_lines.next() {
        if line == "" { continue; }
        let mapping = Vec::from_iter(line.split(" = "));
        let left_right = Vec::from_iter(mapping[1].trim_matches(|c| c == '(' || c == ')').split(", "));
        node_directions_map.insert(String::from(mapping[0]), Directions { left: String::from(left_right[0]), right: String::from(left_right[1]) });
    }
    return (Vec::from_iter(directions.chars()), node_directions_map);
}


fn find_total_steps(directions: &Vec<char>, node_map: &HashMap<String, Directions>) -> usize {
    let mut count = 0;
    let mut curr_position = String::from("AAA");

    while curr_position.as_str() != "ZZZ" {
        match node_map.get(&curr_position) {
            Some(Directions { left: l, right: r }) => {
                if directions[count % directions.len()] == 'L' {
                    curr_position = l.to_string();
                }
                else {
                    curr_position = r.to_string();
                }
            },
            _ => panic!("no such mapping")
        }
        count += 1;
    }
    return count;
}


fn total_steps_last_char(directions: &Vec<char>, node_map: &HashMap<String, Directions>) -> Vec<usize> {
    let mut curr_positions = Vec::from_iter(node_map.keys().filter(|s| s.ends_with('A')).map(|x| (0, x))); // tuple of count to reach node ending in z, and the node

    for i in 0..curr_positions.len() {
        while !curr_positions[i].1.ends_with("Z") {
            match curr_positions[i] {
                (count, pos) => {
                    match node_map.get(pos.as_str()) {
                        Some(Directions {left: l, right: r}) => {
                            if directions[count % directions.len()] == 'L' {
                                curr_positions[i] = (count + 1, l);
                            }
                            else {
                                curr_positions[i] = (count + 1, r);
                            }
                        }
                        _ => panic!("no such mapping")
                    }
                }
            }
        }
    }

    return Vec::from_iter(curr_positions.iter().map(|elem| elem.0)); // returning list of steps for each starting position
}


fn gcd(a: usize, b: usize) -> usize {
    return if b == 0 { a } else { gcd(b, a % b) }
}


fn lcm(a: usize, b: usize) -> usize {
    return (a * b) / gcd(a, b)
}


fn main() {
    let (directions, node_map) = get_file_data("./input.txt");
    let part1_ans = find_total_steps(&directions, &node_map);
    println!("Part 1 answer: {}", part1_ans);

    // lcm (for when a path has to repeat while others are still reaching z)
    let part2_ans = total_steps_last_char(&directions, &node_map).iter().fold(1, |a, b| lcm(a, *b));
    println!("Part 2 answer: {}", part2_ans);
}
